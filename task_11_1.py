class Data:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def dates(self):
        if 1 <= self.day <= 31:
            if 1 <= self.month <= 12:
                if 2022 >= self.year >= 0:
                    return f'Class Data: {self.year, self.month, self.day}'
                else:
                    return f'Ошибка при вводе года'
            else:
                return f'Ошибка при вводе месяца'
        else:
            return f'Ошибка при вводе дня'

    def __str__(self):
        return f'{self.year, self.month, self.day}'


    @classmethod
    def my_method(cls, day: int, month: int, year: int):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    print('Classmethod: ', day, month, year)
                else:
                    print('Ошибка при вводе года')
            else:
                print('Ошибка при вводе месяца')
        else:
            print('Ошибка при вводе дня')

    @staticmethod
    def class_info(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Staticmethod, {day}, {month}, {year}'
                else:
                    return f'Ошибка при вводе года'
            else:
                return f'Ошибка при вводе месяца'
        else:
            return f'Ошибка при вводе дня'

d = Data(11, 3, 1822)
print(d.dates())
Data.my_method(11, 13, 2022)
print(Data.class_info(11, 3, 2027))