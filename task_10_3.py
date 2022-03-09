class Cell:
    def __init__(self, number_cells):
        self.number_cells = int(number_cells)

    def __add__(self, other):
        return f'Сложение клеток: {self.number_cells + other.number_cells}'

    def __sub__(self, other):
        sub = self.number_cells - other.number_cells
        if sub > 0:
            return f'Вычитание клеток: {sub}'
        else:
            return f'Уменьшаемое меньше вычитаемого. Вычитание невозможно'

    def __truediv__(self, other):
        return f'Деление клеток: {self.number_cells // other.number_cells}'

    def __mul__(self, other):
        return f'Умножение клеток: {self.number_cells * other.number_cells}'

    def make_order(self, row):
        result = ''
        for i in range(int(self.number_cells / row)):
            result += f'{"*" * row} \\n'
        result += '*' * (self.number_cells % row)
        return result

cell_1 = Cell(14)
cell_2 = Cell(12)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(7))
print(cell_2.make_order(8))