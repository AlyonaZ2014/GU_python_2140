file_1 = open('6.1.txt', 'r', encoding='utf-8')
new = []
for line in file_1:
    sp = line.split()
    new.append((sp[0], sp[5].replace('"', ''),sp[6]))
print(new)
new_s = tuple(new)
print('\n'.join(map(str, new_s)))
file_1.close()