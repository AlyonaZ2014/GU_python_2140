class Road:
    mass_for_1cm = 25
    thickness = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self):
        mass_asphalt = self._length * self._width * self.mass_for_1cm * self.thickness / 1000
        print(f'Масса асфальта для покрытия всего полотна равна: {round(mass_asphalt)} т')
        return mass_asphalt


road = Road(5000, 20)
road.mass_asphalt()
road = Road(500, 20)
road.mass_asphalt()
road = Road(50000, 20)
road.mass_asphalt()