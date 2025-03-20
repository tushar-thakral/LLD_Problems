from elevator_system.lift import Lift


class LiftManager:
    def __init__(self):
        self.floors_count = 0
        self.lifts_count = 0
        self.lifts_capacity = 0
        self.helper = None
        self.lifts = []

    def init(self, floors, lifts, lifts_capacity, helper):
        """
        Initializes the elevator system.
        Args:
            floors (int): The number of floors in the building.
            lifts (int): The number of lifts in the system.
            lifts_capacity (int): The maximum number of people per lift.
            helper (Helper11): Helper class for printing and other actions.
        """
        self.floors_count = floors
        self.lifts_count = lifts
        self.lifts_capacity = lifts_capacity
        self.helper = helper
        self.lifts = [Lift(floors, lifts_capacity) for _ in range(lifts)]
        # self.helper.println("Lift system initialized ...")

    def request_lift(self, floor, direction):
        """
        User presses the outside UP or DOWN button outside the lift.
        Args:
            floor (int): The current floor.
            direction (str): The direction ('U' for up or 'D' for down).

        Returns:
            int: Index of the selected lift or -1 if no lift is available.
        """
        lift_index = -1
        time_taken = -1
        for i, lift in enumerate(self.lifts):
            time = lift.get_time_to_reach_floor(floor, direction)
            if time < 0 or lift.count_people(floor, direction) >= self.lifts_capacity:
                continue
            if time_taken < 0 or time < time_taken:
                time_taken = time
                lift_index = i
        if lift_index >= 0:
            self.lifts[lift_index].add_incoming_request(floor, direction)
        return lift_index

    def press_floor_button_in_lift(self, lift_index, floor):
        """
        User presses the floor button inside the lift.
        Args:
            lift_index (int): Index of the lift.
            floor (int): The floor button pressed.
        """
        lift = self.lifts[lift_index]
        lift.add_outgoing_request(floor, lift.get_move_direction())

    def get_lift_state(self, lift_index):
        """
        Returns the current state of the lift.
        Args:
            lift_index (int): Index of the lift.

        Returns:
            str: String representation of the lift's state.
        """
        if lift_index < 0 or lift_index >= len(self.lifts):
            return ""
        lift = self.lifts[lift_index]
        return f"{lift.get_current_floor()}-{lift.get_move_direction()}-{lift.get_current_people_count()}"

    def tick(self):
        """
        This method is called every second to update the lift states.
        """
        for lift in self.lifts:
            lift.tick()
