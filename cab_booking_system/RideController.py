from cab_booking_system.Fare import Fare
from cab_booking_system.Location import Location
from cab_booking_system.Ride import Ride
from cab_booking_system.User import User


class RideController:

    def __init__(self, cab_controller, pricing_strategy):
        self.rides = {}
        self.cab_controller = cab_controller
        self.pricing_strategy = pricing_strategy

    def calculate_distance(self, location1: Location, location2: Location) -> float:
        import math

        lon1, lat1 = location1.longitude, location1.latitude
        lon2, lat2 = location2.longitude, location2.latitude

        R = 6371000  # radius of Earth in meters
        phi_1 = math.radians(lat1)
        phi_2 = math.radians(lat2)

        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = math.sin(delta_phi / 2.0) ** 2 + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2

        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        meters = R * c  # output distance in meters
        meters = round(meters, 3)

        return meters

    def find_cab(self, pickup_location, drop_location):
        potential_cabs = []
        for cab in self.cab_controller.cab_list:
            if cab.status == "IDLE" and self.calculate_distance(pickup_location, cab.current_location) < distance_radius:
                potential_cabs.append(cab)
        for cab in potential_cabs:
            cab.request_ride(pickup_location, drop_location)
        return potential_cabs[0]

    def add_ride(self, user: User, pickup_location: Location, drop_location: Location, distance_radius: float):
        cab = self.find_cab(pickup_location, drop_location)
        ride = Ride(id="ABC", fare=Fare(0), pickup_location=pickup_location, drop_location=drop_location, user=user, driver=cab.driver, status="ACTIVE")
        self.rides[ride.id] = ride
        ride.set_status("ACTIVE")
        ride.user.ongoing_rides()
        ride.driver.ongoing_rides()

    def end_ride(self, ride_id: str):
        self.rides[ride_id].set_status("COMPLETED")
        ride = self.rides[ride_id]
        self.rides[ride_id].set_fare(self.calculate_fare(ride.pickup_location, ride.drop_location))
        ride.user.ongoing_rides()
        ride.driver.ongoing_rides()
        ride.user.completed_rides()
        ride.driver.completed_rides()


    def calculate_fare(self, pickup_location: Location, drop_location: Location):
        return 10