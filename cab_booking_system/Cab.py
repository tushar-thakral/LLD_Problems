from Driver import Driver
from Location import Location


class Cab:

    def __init__(self, id:str, status: str, current_location: Location, driver: Driver):
        self.id = id
        self.status = status
        self.current_location = current_location
        self.driver = driver

    def current_location(self) -> Location:
        return self.current_location

    def driver(self) -> Driver:
        return self.driver

    def set_current_location(self, location: Location):
        self.current_location = location

    def status(self) -> str:
        return self.status

    def id(self) -> str:
        return self.id

    def request_ride(self, pickup_location: Location, drop_location: Location):
        self.driver.ride_request(pickup_location, drop_location)