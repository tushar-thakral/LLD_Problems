from cab_booking_system.CabController import CabController
from cab_booking_system.DriverController import DriverController
from cab_booking_system.LocationUpdateController import LocationUpdateController
from cab_booking_system.UserController import UserController


class CabBookingPlatform:

    def __init__(self, user_controller: UserController, driver_controller: DriverController, cab_controller: CabController, location_update_controller: LocationUpdateController):
        self.user_controller = user_controller
        self.driver_controller = driver_controller
        self.cab_controller = cab_controller
        self.location_update_controller = location_update_controller
