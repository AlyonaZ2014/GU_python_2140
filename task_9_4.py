class Car:

    def __init__(self, speed, color, name, is_police=bool):
        self.__speed = speed
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Вы поехали')

    def stop(self):
        self.speed = 0
        print(f'Вы остановились')

    def turn(self, direction):
        if self.speed > 0:
            print(f'Поворот {direction}')
        else:
            print('Вы остановились')

    def show_speed(self):
        print(f'Текущая скорость {self.speed} км/ч')

class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')

class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости {self.speed} км/ч')
        else:
            print(f'Скорость {self.speed} км/ч')

class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)

def rezultat(game):
    game.go(40)
    game.show_speed()
    game.turn('направо')
    game.stop()
    game.show_speed()
    game.go(90)
    game.show_speed()
    game.turn('налево')
    game.go(160)
    game.show_speed()
    game.stop()
    print(end='\n')
    return rezultat


car = Car('серый', 'Вольво', False)
rezultat(car)

pol = PoliceCar('белый', 'лада', True)
rezultat(pol)

town = TownCar('красный', 'Шкода', False)
rezultat(town)

wrc = WorkCar('красный', 'рено', False)
rezultat(wrc)

spc = SportCar('синий', 'бмв', False)
rezultat(spc)

