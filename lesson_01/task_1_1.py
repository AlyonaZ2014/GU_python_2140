#1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
#Формат вывода результата:

#до минуты: <s> сек;
#до часа: <m> мин <s> сек;
#до суток: <h> час <m> мин <s> сек;
#в остальных случаях: <d> дн <h> час <m> мин <s> сек.
duration = int(input('Введите время в секундах: '))
if duration <= 60: #сек
    print('Время: ', duration, 'сек')
elif 60 < duration <= 3600:#мин
    m = 1
    while m <= duration:
        min = duration // 60
        sec = duration % 60
        m = m + 1

    print ('Время: ',  min, 'мин', sec, 'сек')

elif 3600 < duration <= 86400:
    h = 1
    while h <= duration:
        hour = duration // 3600
        remainder_hour = duration % 3600
        min = remainder_hour // 60
        sec = remainder_hour % 60
        h = h + 1

    print('Время: ', hour,'час', min, 'мин', sec, 'сек')
else:
    d = 1
    while d <= duration:
        day = duration // 86400
        remainder_day = duration % 86400
        hour = remainder_day // 3600
        remainder_hour = remainder_day % 3600
        min = remainder_hour // 60
        sec = remainder_hour % 60
        d = d + 1
    print('Время: ', day, 'дн', hour, 'час', min, 'мин', sec, 'сек')