from parking_spot import ParkingSpot
from vehicle import Vehicle

class Level:

    def __init__(self, floor: int, num_spots: int):
        self.floor = floor
        self.parking_spots = [ ParkingSpot(index) for index in range(num_spots) ]

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if spot.is_available() and spot.get_vehicle_type() == vehicle.get_type():
                spot.park_vehicle(vehicle)
                return True
        return False

    def remove_vehicle(self, vehicle: Vehicle) -> bool:
        for spot in self.parking_spots:
            if not spot.is_available() and spot.get_parked_vehicle() == vehicle:
                spot.remove_vehicle()
                return True
        return False

    def display_availability(self) -> None:
        print(f"Level {self.floor} Availability:")
        for spot in self.parking_spots:
            print(f"Spot {spot.get_spot_number()}: {'Available' if spot.is_available() else 'Occupied'}")
