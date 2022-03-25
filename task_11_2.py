import traceback

class OwnError(Exception):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __truediv__():
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            if b == 0:
                raise OwnError("Делить на ноль нельзя!")
            else:
                rez = round(a / b, 2)
                return rez
        except ValueError:
            print('Вы ввели не число')
        except OwnError as err:
            print(err)
    print(__truediv__())