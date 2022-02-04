lst =  ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for i in range (len(lst)):
    lst_1 = lst[i].split(" ")
    #print(lst_1)
    name = lst_1[-1].title()
  #  print(name)
    greeting = f'Привет, {name}!'
    print(greeting)