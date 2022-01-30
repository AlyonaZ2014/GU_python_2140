user_namber = int(input('Введите число от 0 до 1000: '))
odd_namber = 1
while odd_namber  <= user_namber:
    odd_namber = odd_namber + 1
    if odd_namber % 2 == 0:
       continue
    else:
        involution = odd_namber ** 3
        #print(involution)

    c = 1
    while c <= involution:
        c = c + 1

        if 0 < involution < 10:
            remainder = involution % 10
            summa = remainder
        elif 10 <= involution < 100:
            integen = involution // 10
            #print(integen)
            remainder = involution % 10
            #print(remainder)
            summa = remainder + remainder

        elif 100 <= involution < 1000:
            integen = involution // 10
            integen_1 = integen // 10
            remainder = involution % 10
            remainder_1 = integen % 10
            summa = integen_1 + remainder + remainder_1
        elif 1000 <= involution < 10000: #необходимые переменные для суммы обозначу: int_1...int_x, rem_1...rem_x
            int_1 = involution // 1000
            rem_1 = involution % 10
            integen_1 = involution // 100
            rem_2 = integen_1 % 10
            remainder_1 = involution % 100
            int_2 = remainder_1 // 10
            summa = int_1 + rem_1 + rem_2 + int_2
        elif 10000 <= involution < 100000:
            int_1 = involution // 10000
            rem_1 = involution % 10
            integen_1 = involution // 1000
            rem_2 = integen_1 % 10
            integen_2 = involution // 100
            rem_3 = integen_2 % 10
            integen_3 = involution // 10
            rem_4 = integen_3 % 10
            summa = int_1 + rem_1 + rem_2 + rem_3 + rem_4
        elif 100000 <= involution < 1000000:
            int_1 = involution // 100000
            rem_1 = involution % 10
            integen_1 = involution // 10000
            rem_2 = integen_1 % 10
            integen_2 = involution // 1000
            rem_3 = integen_2 % 10
            integen_3 = involution // 100
            rem_4 = integen_3 % 10
            remainder_1 = involution % 100
            int_2 = remainder_1 // 10
            summa = int_1 + rem_1 + rem_2 + rem_3 + rem_4 + int_2
        elif 1000000 <= involution < 10000000:
            int_1 = involution // 1000000
            rem_1 = involution % 10
            integen_1 = involution // 100000
            rem_2 = integen_1 % 10
            integen_2 = involution // 10000
            rem_3 = integen_2 % 10
            integen_3 = involution // 1000
            rem_4 = integen_3 % 10
            integen_4 = involution // 100
            rem_5 = integen_4 % 10
            integen_5 = involution // 10
            rem_6 = integen_5 % 10
            summa = int_1 + rem_1 + rem_2 + rem_3 + rem_4 + rem_5 + rem_6
        elif 10000000 <= involution < 100000000:
            int_1 = involution // 10000000
            rem_1 = involution % 10
            integen_1 = involution // 1000000
            rem_2 = integen_1 % 10
            integen_2 = involution // 100000
            rem_3 = integen_2 % 10
            integen_3 = involution // 10000
            rem_4 = integen_3 % 10
            integen_4 = involution // 1000
            rem_5 = integen_4 % 10
            integen_5 = involution // 100
            rem_6 = integen_5 % 10
            integen_6 = involution // 10
            rem_7 = integen_6 % 10
            summa = int_1 + rem_1 + rem_2 + rem_3 + rem_4 + rem_5 + rem_6 + rem_7
        elif 100000000 <= involution < 1000000000:
            int_1 = involution // 100000000
            rem_1 = involution % 10
            integen_1 = involution // 10000000
            rem_2 = integen_1 % 10
            integen_2 = involution // 1000000
            rem_3 = integen_2 % 10
            integen_3 = involution // 100000
            rem_4 = integen_3 % 10
            integen_4 = involution // 10000
            rem_5 = integen_4 % 10
            integen_5 = involution // 1000
            rem_6 = integen_5 % 10
            integen_6 = involution // 100
            rem_7 = integen_6 % 10
            integen_7 = involution // 10
            rem_8 = integen_7 % 10
            summa = int_1 + rem_1 + rem_2 + rem_3 + rem_4 + rem_5 + rem_6 + rem_7 + rem_8
        else: 
            int_1 = involution // 1000000000
            rem_1 = involution % 10
            integen_1 = involution // 100000000
            rem_2 = integen_1 % 10
            integen_2 = involution // 10000000
            rem_3 = integen_2 % 10
            integen_3 = involution // 1000000
            rem_4 = integen_3 % 10
            integen_4 = involution // 100000
            rem_5 = integen_4 % 10
            integen_5 = involution // 10000
            rem_6 = integen_5 % 10
            integen_6 = involution // 1000
            rem_7 = integen_6 % 10
            integen_7 = involution // 100
            rem_8 = integen_7 % 10
            integen_8 = involution // 10
            rem_9 = integen_8 % 10
            summa = int_1 + rem_1 + rem_2 + rem_3 + rem_4 + rem_5 + rem_6 + rem_7 + rem_8 + rem_9
    if summa % 7 == 0:
        s = summa
        print( odd_namber, '^3: ', involution, 'sum: ', user_namber, '[ ', s, ']')