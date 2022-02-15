tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
groups = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '11A', '11B'
]


def my_function(tutors, groups):
    for i in range(len(tutors)):
        yield (tutors[i], groups[i] if len(groups) > i else None)

gen = my_function(tutors, groups)
print(type(gen))
for el in gen:
    print(f'{el}')
