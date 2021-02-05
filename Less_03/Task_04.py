"""
4 Определить, какое число в массиве встречается чаще всего.

"""

import datetime
import random

SIZE = 5_000_000
MIN_ITEM = 0
MAX_ITEM = 200
print(f"{datetime.datetime.now()} - Начинаю собирать массив")
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(array)
array_c = array.copy()
cont = [0] * 2

for i in set(array):
    k = 0
    b = True
    s = 0  # позиция элемента, чтоб продолжить с того же места

    print(f"{datetime.datetime.now()} - Я тут, ищу число {i}")
    while b:
        try:
            # array_c.remove(i)  # долго работает с большим объемом
            s = array_c.index(i, s)
            array_c.pop(s)

            k += 1
        except ValueError:
            b = False

    if cont[0] < k:
        cont[0], cont[1] = k, i

print(f'Цифра {cont[1]} по вторяется {cont[0]} раз')
