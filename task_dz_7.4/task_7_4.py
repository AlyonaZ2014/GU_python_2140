import os
from os.path import join

for r, d, f in os.walk(r'some_data'):
    siz = []
    for fale in f:
        size = os.stat(join(r, fale)).st_size
        siz.append(size)
    min_siz = min(siz)
    max_siz = max(siz)
    # print(min_siz, max_siz)

rez = {}
for key in range(1, len(str(max_siz)) + 1):
    rez[10 ** key] = 0

for value in siz:

    v = len(str(value))
    min_size = 10 ** (v - 1)
    max_size = 10 ** v
    if min_size < value < max_size:
        rez[max_size] += 1
# print(rez)

for key, value in rez.items():
    print(key, ":", value)
