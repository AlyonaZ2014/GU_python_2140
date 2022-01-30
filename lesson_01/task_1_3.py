#Реализовать склонение слова «процент» во фразе "N процентов"
# Вывести эту фразу на экран отдельной строкой для каждого
# из чисел в интервале от 1 до 150:
user_namber = int(input('Введите количество процентов от 0 до 150: '))
namber = 0
while namber <= user_namber:
    #namber = namber + 1
    if namber == 11:
         print(namber, 'процентов')
    elif namber == 12:
         print(namber, 'процентов')
    elif namber == 13:
         print(namber, 'процентов')
    elif namber == 14:
         print(namber, 'процентов')
    elif namber % 10 > 1 and namber % 10 < 5:
         print(namber, 'процентa')
    elif namber % 10 == 1:
         print(namber, 'процент')
    else:
         print(namber, 'процентов')
    #print(namber)
    namber = namber + 1

