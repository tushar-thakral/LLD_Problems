from Location import Location


class User:

    def __init__(self, id:str, name:str, pickup_location: Location, drop_location: Location):
        self.id = id
        self.name = name
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.ongoing_rides = []
        self.completed_rides = []

    def pickup_location(self) -> Location:
        return self.pickup_location

    def drop_location(self) -> Location:
        return self.drop_location

    def id(self) -> str:
        return self.id

    def ongoing_rides(self):
        return self.ongoing_rides

    def completed_rides(self):
        return self.completed_rides
