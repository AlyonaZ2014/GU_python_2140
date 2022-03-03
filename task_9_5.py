class Stationery:
    def __init__(self, title):
        self.title = title

class Pen(Stationery):
    def draw(self):
        rez = f'Запуск отрисовки {self.title}'
        return rez

class Pencil(Stationery):
    def draw(self):
        rez = f'Запуск отрисовки {self.title}'
        return rez

class Handle(Stationery):
    def draw(self):
        rez = f'Запуск отрисовки {self.title}'
        return rez

pen = Pen('ручка')
print(pen.draw())
pencil = Pencil('карандаш')
print(pencil.draw())
handle = Handle('маркер')
print(handle.draw())