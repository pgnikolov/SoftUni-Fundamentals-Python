class Town:

    def __init__(self, name: str):
        self.name = name
        self.latitude = "0°N"
        self.longtitude = "0°E"

    def set_latitude(self, latitude):
        self.latitude = latitude

    def set_longitude(self, longtitude):
        self.longtitude = longtitude

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longtitude: {self.longtitude}"


town = Town("Sofia")

town.set_latitude("42° 41\' 51.04\" N")

town.set_longitude("23° 19\' 26.94\" E")

print(town)