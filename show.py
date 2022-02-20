import sys
user_namber = sys.argv[1:]
with open('bakery.csv', 'r', encoding='utf-8') as f:
    if len(user_namber) > 1:
        start_i = int(user_namber[0])
        end_i = int(user_namber[1])
    elif len(user_namber) == 0:
        start_i = 0
        end_i = sum(1 for line in f)
        f.seek(0)
    for i, line in enumerate(f):
        if start_i <= i + 1 <= end_i:
            print(line.strip())
