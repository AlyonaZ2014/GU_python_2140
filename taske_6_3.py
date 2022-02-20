d = {}
new_1 = []
name = []
with open('task_3_4_hobby.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        new_1.append(line)
with open('task_3_4_FIO.txt', 'r', encoding='utf-8') as file_1:
    for line in file_1:
        summa = ''
        sp = line.split(',')
        for el in sp:
            name1 = []
            summa += el[0]
        name.append(summa)
# print(name)
# print(new_1)
hobby = list(map(lambda x:x.strip(),new_1))
# for i in range(0, len(name)):
#     d[name[i]] = hobby[i]
from itertools import zip_longest
d = {k: v for k, v in zip_longest(name, hobby) if k is not None}
print(d)
import json
with open('rezultat.json', 'w', encoding='utf-8') as file_1:
    json.dump(d, file_1, ensure_ascii=False)



