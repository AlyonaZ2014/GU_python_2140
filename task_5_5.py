# Задан список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать из этих элементов список с сохранением порядка их следования в исходном списке
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique = set()
tmp = set()
for el in src:
    if el not in tmp:
        unique.add(el)
    else:
        unique.discard(el)
    tmp.add(el)

unique_1 = [el for el in src if el in unique]
print(unique_1)