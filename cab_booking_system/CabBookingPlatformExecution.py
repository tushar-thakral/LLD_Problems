from Cab import Cab
from CabBookingPlatform import CabBookingPlatform
from CabController import CabController
from Driver import Driver
from DriverController import DriverController
from Location import Location
from LocationUpdateController import LocationUpdateController
from PricingStrategy import DynamicPricingStrategy
from RideController import RideController
from User import User
from UserController import UserController


def execution():
    # id: str, name: str, pickup_location: Location, drop_location: Location)

    delivery_agent_location = Location(longitude=77.647, latitude=12.908)  # HSR Layout

    # Restaurant1 Creation
    restaurant1_location = Location(longitude=77.758, latitude=12.994)  # Whitefield

    # Restaurant2 Creation
    restaurant2_location = Location(longitude=77.661, latitude=12.903)  # Haralur

    # Consumer1 Creation
    consumer1_location = Location(longitude=77.697, latitude=12.959)  # Marathahalli

    # Consumer2 Creation
    consumer2_location = Location(longitude=77.625, latitude=12.931)  # Koramangala

    user1 = User("AB", delivery_agent_location, restaurant1_location)
    driver1 = Driver("cd", "ef")
    driver2 = Driver("se", "eg")
    cab1 = Cab("aa", "IDLE", restaurant2_location, driver1)
    cab2 = Cab("bb", "IDLE", consumer1_location, driver2)

    user_controller = UserController()
    user_controller.add_user(user1)
    print(user1.id)
    print(user_controller.users)
    driver_controller = DriverController()
    driver_controller.add_driver(driver1)
    driver_controller.add_driver(driver2)
    ride_controller = RideController()
    cab_controller = CabController()
    pricing_strategy = DynamicPricingStrategy()
    location_controller = LocationUpdateController()
    platform = CabBookingPlatform(user_controller, driver_controller, cab_controller, location_controller)
    print(platform.user_controller.users)