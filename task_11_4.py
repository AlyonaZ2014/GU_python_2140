class Complex_namber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a} + {self.b}j'

    def __add__(self, other):
        return f'Сложение: {self.a + other.a} + {self.b + other.b}j'

    def __sub__(self, other):
        return f'Вычитание: {self.a - other.a} - {self.b - other.b}j'

    def __mul__(self, other):
        return f'Произведение: {(self.a * other.a) - (self.b * other.b)} *{(self.a * other.b) + (self.b * other.a)}j'

x = Complex_namber(4, 15)
y = Complex_namber(9, -2)
c_1 = x + y
c_2 = x * y
c_3 = x - y

print('Комплексное число 1: ', x)
print('Комплексное число 2: ', y)
print(c_1)
print(c_2)
print(c_3)

