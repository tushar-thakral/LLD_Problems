class Location:

    def __init__(self, longitude: float, latitude: float):
        self.longitude = longitude
        self.latitude = latitude

    @property
    def longitude(self) -> float:
        return self.longitude

    @property
    def latitude(self) -> float:
        return self.latitude
