from cab_booking_system.Cab import Cab
from cab_booking_system.Location import Location


class CabController:

    def __init__(self):
        self.cabs = {}

    def add_cab(self, cab: Cab):
        self.cabs[cab.id] = cab

    def remove_cab(self, cab_id: str):
        self.cabs.pop(cab_id)

    def cab_list(self):
        return self.cabs

    def update_cab_location(self, cab_id: str, location: Location):
        self.cabs[cab_id].set_current_location(location)