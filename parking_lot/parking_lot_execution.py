from parking_lot_base import ParkingLot
from level import Level
from car import Car
from bike import Bike
from truck import Truck

class ParkingLotExecution:

    def run(self):
        parking_lot = ParkingLot.get_instance()
        parking_lot.add_level(Level(1, 5))
        parking_lot.add_level(Level(2, 4))

        car = Car("ABC123")
        truck = Truck("XYZ789")
        bike = Bike("M1234")

        # Park vehicles
        parking_lot.park_vehicle(car)
        parking_lot.park_vehicle(truck)
        parking_lot.park_vehicle(bike)

        # Display availability
        parking_lot.display_availability()

        # Remove vehicle
        parking_lot.remove_vehicle(bike)

        # Display updated availability
        parking_lot.display_availability()

if __name__ == "__main__":
    parking_lot = ParkingLotExecution()
    ParkingLotExecution.run(parking_lot)