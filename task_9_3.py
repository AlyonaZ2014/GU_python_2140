class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        __income__ = {'оклад': int(wage), 'премия': int(bonus)}
        self.name = name
        self.surname = surname
        self.position = position
        self.__income__ = __income__

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self.__income__.values())

p = Position('Анна', 'Михайловна', 'техник', '10000', '5000')
print(p.get_full_name(), p.get_total_income())
p = Position('Игорь', 'Алексеевич', 'электрик', '19000', '9000')
print(p.get_full_name(), p.get_total_income())