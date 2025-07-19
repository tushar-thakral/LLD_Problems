from cab_booking_system.Driver import Driver


class DriverController:

    def __init__(self):
        self.drivers = {}

    def add_driver(self, driver: Driver):
        self.drivers[driver.id] = driver

    def remove_driver(self, driver: Driver):
        self.drivers.pop(driver.id)
