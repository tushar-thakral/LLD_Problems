from collections import defaultdict

from elevator_system.lift_states import MovingUpState, MovingDownState, IdleState, MovingUpToPickFirstState, \
    MovingDownToPickFirstState


class Lift:
    def __init__(self, floors, capacity):
        self.current_floor = 0
        self.floors = floors
        self.capacity = capacity
        self.incoming_requests_count = set()
        self.outgoing_requests_count = defaultdict(int)
        self.moving_up_state = MovingUpState(self)
        self.moving_down_state = MovingDownState(self)
        self.idle_state = IdleState(self)
        self.moving_up_to_pick_first = MovingUpToPickFirstState(self)
        self.moving_down_to_pick_first = MovingDownToPickFirstState(self)
        self.state = self.idle_state

    def get_current_people_count(self):
        return sum(self.outgoing_requests_count.values())

    def get_time_to_reach_floor(self, floor, direction):
        return self.state.get_time_to_reach_floor(floor, direction)

    def add_incoming_request(self, floor, direction):
        if self.state.get_direction() == 'I':
            if floor == self.current_floor:
                self.set_state(direction)
            else:
                if floor > self.current_floor:
                    self.state = self.moving_up_state if direction == 'U' else self.moving_up_to_pick_first
                else:
                    self.state = self.moving_down_state if direction == 'D' else self.moving_down_to_pick_first
        self.incoming_requests_count.add(floor)

    def add_outgoing_request(self, floor, direction):
        self.outgoing_requests_count[floor] += 1

    def count_people(self, floor, direction):
        return self.state.count_people(floor, direction)

    def get_move_direction(self):
        return self.state.get_direction()

    def get_current_floor(self):
        return self.current_floor

    def tick(self):
        self.state.tick()
        if not self.outgoing_requests_count and not self.incoming_requests_count:
            self.set_state('I')

    def set_state(self, direction):
        if direction == 'U':
            self.state = self.moving_up_state
        elif direction == 'D':
            self.state = self.moving_down_state
        else:
            self.state = self.idle_state

    def set_current_floor(self, current_floor):
        self.current_floor = current_floor
