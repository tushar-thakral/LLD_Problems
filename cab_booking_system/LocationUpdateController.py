from cab_booking_system.Location import Location


class LocationUpdateController:

    def __init__(self, cab_controller):
        self.cab_controller = cab_controller

    def update_cab_location(self, cab_id: str, location: Location):
        self.cab_controller.update_cab_location(cab_id, location)