class LiftState:
    def __init__(self, lift):
        self.lift = lift

    def get_direction(self):
        return 'I'

    def get_time_to_reach_floor(self, floor, direction):
        return 0

    def count_people(self, floor, direction):
        return 0

    def tick(self):
        pass


class MovingUpState(LiftState):
    def get_direction(self):
        return 'U'

    def get_time_to_reach_floor(self, floor, direction):
        if direction != 'U' or floor < self.lift.get_current_floor():
            return -1
        return floor - self.lift.get_current_floor()

    def count_people(self, floor, direction):
        if direction != 'U':
            return 0
        return sum(v for f, v in self.lift.outgoing_requests_count.items() if f > floor)

    def tick(self):
        self.lift.incoming_requests_count.discard(self.lift.get_current_floor())
        # check if idle state has been achieved i.e. if there were requests on previous floor but no one entered
        if not self.lift.incoming_requests_count and not self.lift.outgoing_requests_count:
            return
        self.lift.set_current_floor(self.lift.get_current_floor() + 1)
        self.lift.outgoing_requests_count.pop(self.lift.get_current_floor(), None)


class MovingDownState(LiftState):
    def get_direction(self):
        return 'D'

    def get_time_to_reach_floor(self, floor, direction):
        if direction != 'D' or floor > self.lift.get_current_floor():
            return -1
        return self.lift.get_current_floor() - floor

    def count_people(self, floor, direction):
        if direction != 'D':
            return 0
        return sum(v for f, v in self.lift.outgoing_requests_count.items() if f < floor)

    def tick(self):
        self.lift.incoming_requests_count.discard(self.lift.get_current_floor())
        # check if idle state has been achieved i.e. if there were requests on previous floor but no one entered
        if not self.lift.incoming_requests_count and not self.lift.outgoing_requests_count:
            return
        self.lift.set_current_floor(self.lift.get_current_floor() - 1)
        self.lift.outgoing_requests_count.pop(self.lift.get_current_floor(), None)


class IdleState(LiftState):
    def get_direction(self):
        return 'I'

    def get_time_to_reach_floor(self, floor, direction):
        return abs(floor - self.lift.get_current_floor())


class MovingUpToPickFirstState(LiftState):
    def get_direction(self):
        return 'U'

    def get_time_to_reach_floor(self, floor, direction):
        next_stop = self.next_stop()
        if direction != 'D' or floor > next_stop:
            return -1
        return next_stop - self.lift.get_current_floor() + next_stop - floor

    def next_stop(self):
        return max(self.lift.incoming_requests_count, default=-1)

    def tick(self):
        self.lift.set_current_floor(self.lift.get_current_floor() + 1)
        if self.lift.get_current_floor() == self.next_stop():
            self.lift.set_state('D')


class MovingDownToPickFirstState(LiftState):
    def get_direction(self):
        return 'D'

    def get_time_to_reach_floor(self, floor, direction):
        next_stop = self.next_stop()
        if direction != 'U' or floor < next_stop:
            return -1
        if next_stop < 0:
            next_stop = floor
        return self.lift.get_current_floor() - next_stop + floor - next_stop

    def next_stop(self):
        return min(self.lift.incoming_requests_count, default=-1)

    def tick(self):
        self.lift.set_current_floor(self.lift.get_current_floor() - 1)
        if self.lift.get_current_floor() == self.next_stop():
            self.lift.set_state('U')