lst = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# lst[3] = '"17"'
# lst[1] = '"05"'
# lst[-2] = '"+05"'
# print(lst)
# message = ' '. join (lst)
# print(message)
lst_1 = [] #наполняю пустой список
for i in lst:
    if i.isdigit(): #проверка на цифры
        lst_1.append(f' "{i.zfill(2)}"') #нули добавляем
    elif i[0] in ('+' or "-"):
        lst_1.append(f' "{i[0]}{i[1:].zfill(2)}"') #+/-срез
    else:
        lst_1.append(i)
message = ' '. join (lst_1)
print(message)