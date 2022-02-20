import sys
sale = sys.argv[1]
file_1 = open('bakery.csv', 'a', encoding='utf-8')
file_1.write(sale + '\n')
file_1.close()