from parking_lot.bike import Bike
from parking_lot.car import Car
from parking_lot.level import Level
from parking_lot.parking_lot_base import ParkingLot
from parking_lot.truck import Truck


def test_parking_lot():

    parking_lot = ParkingLot()
    parking_lot.add_level(Level(1, 5))
    parking_lot.add_level(Level(2, 4))
    car = Car("ABC123")
    truck = Truck("XYZ789")
    bike = Bike("M1234")

    assert parking_lot.park_vehicle(car) == True
    assert parking_lot.park_vehicle(truck) == False
    assert parking_lot.remove_vehicle(bike) == False


