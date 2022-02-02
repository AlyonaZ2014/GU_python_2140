lst = [57.8, 46.67, 83, 434.70, 43.20, 578.94, 634.57, 563.72, 643.76, 68.93, 45.00, 56.42]
print(lst)
str_lst = [str(x) for x in lst]
str_lst_1 = ' '.join(str_lst)
#print(str_lst_1)
for i in lst:
    rub = int(i)
    kk = (i - rub) * 100
    str_price = f'{rub} руб {kk:02.0f} коп'
    #print(a)
    print(str_price, end= ",")
print(', '.join(str_price))

asc_number = lst
asc_number.sort()
print(asc_number)
print('Доказательство операции in place: ', '\n', 'id перед сортировкой: ', id(lst), '\n', 'id после сортировки: ', id(asc_number))

descending = sorted(lst, reverse= True)
print(descending)
print('Новый объект: ', '\n', 'id перед сортировкой: ', id(lst), '\n', 'id после сортировки: ', id(descending))

#5 самых дорогих товаров:

five_max = descending[:5]
print(five_max, type(five_max))
five_max_1 = [str(x) for x in five_max]
d = '\n'.join(five_max_1)
print('5 самых дорогих товаров: ')
print('\n'.join(five_max_1))
