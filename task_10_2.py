from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, textil):
        self.textil = textil

    @abstractmethod
    def fabric_consumption(self):
        pass

    def __add__(self, other):
        return round((self.textil / 6.5 + 0.5) + (2 * other.textil + 0.3))

class Coat(Clothes):
    def __init__(self, textil):
        super().__init__(textil)

    @property
    def fabric_consumption(self):
        return round(self.textil / 6.5 + 0.5)

class Costume(Clothes):
    def __init__(self, textil):
        super().__init__(textil)

    @property
    def fabric_consumption(self):
        return round(2 * self.textil + 0.3)

coat = Coat(48)
costume = Costume(52)
print('Для пальто требуется: ', coat.fabric_consumption, 'ткани')
print('Для костюма требуется: ', costume.fabric_consumption, 'ткани')
print('Всего требуется ткани: ', coat + costume)