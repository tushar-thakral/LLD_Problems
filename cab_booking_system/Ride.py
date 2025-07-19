from cab_booking_system.Driver import Driver
from cab_booking_system.Fare import Fare
from cab_booking_system.Location import Location
from cab_booking_system.User import User


class Ride:

    def __init__(self, id: str, fare: Fare, pickup_location: Location, drop_location: Location, user: User, driver: Driver, status: str):
        self.id = id
        self.fare = fare
        self.pickup_location = pickup_location
        self.drop_location = drop_location
        self.user = user
        self.driver = driver
        self.status = status

    def get_status(self) -> str:
        return self.status

    def set_status(self, status):
        self.status = status

    def set_fare(self, ride_fare: float):
        self.fare.set_fare(ride_fare)

    def pickup_location(self) -> Location:
        return self.pickup_location

    def drop_location(self) -> Location:
        return self.drop_location

    def id(self) -> str:
        return self.id