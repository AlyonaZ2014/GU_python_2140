from itertools import cycle

from time import sleep


class TrafficLight:
    __color = cycle([
        {'цвет': 'красный', 'время': 7},
        {'цвет': 'желтый', 'время': 2},
        {'цвет': 'зеленый', 'время': 2},
        {'цвет': 'желтый', 'время': 2}

    ])

    def __init__(self, __init_colors='Красный', __change_count=6):
        self.change_count = __change_count

    def running(self):
        i = 0
        while i < self.change_count:
            light = next(self.__color)
            print(f"Сигнал {light['цвет']}")
            sleep(light['время'])
            i += 1
        return 

rez_light = TrafficLight()
rez_light.running()