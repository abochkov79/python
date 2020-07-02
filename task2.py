class Road:
    _length = 100
    _width = 5

    def __init__(self, road_length, road_width):
        self._length = road_length
        self._width = road_width

    def asphalt_mass(self):
        print(f"Масса асфальта, необходимого для покрытия дорожного полотна длиной {self._length}м и шириной {self._width}м = {self._length * self._width * 25 * 5 / 1000} тонн")


myRoad = Road(5000, 20)
myRoad.asphalt_mass()
