n = int(input('Введите положительное число: '))

def iterator_with_yield(start = 1, stop = n, step = 2):
    rez =  start
    while rez <= stop:
        yield rez
        rez += step
gen1 = iterator_with_yield(start = 1, stop = n, step = 2)
for i in gen1:
    print(f'{i} \nnext(gen1)')