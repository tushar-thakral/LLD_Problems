from cab_booking_system.Location import Location


class Driver:

    def __init__(self, id:str, name:str):
        self.id = id
        self.name = name
        self.ongoing_rides = []
        self.completed_rides = []

    def id(self) -> str:
        return self.id

    def ride_request(self, pickup_location: Location, drop_location: Location):
        return True

    def ongoing_rides(self):
        return self.ongoing_rides

    def completed_rides(self):
        return self.completed_rides