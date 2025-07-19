class Fare:

    def __init__(self, ride_fare: float):
        self.ride_fare = ride_fare

    def get_fare(self) -> float:
        return self.ride_fare

    def set_fare(self, ride_fare: float):
        self.ride_fare = ride_fare