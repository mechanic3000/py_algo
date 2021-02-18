"""
3 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

import random
import sys

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def get_vol(i)->int:
    return sys.getsizeof(i)

for i, item in enumerate(array):
    try:
        if item < min_item[1]:
            min_item[0], min_item[1] = i, item
    except NameError:
        min_item = [i, item]

    try:
        if item > max_item[1]:
            max_item[0], max_item[1] = i, item
    except NameError:
        max_item = [i, item]

sum = int()
sum += get_vol(min_item)
sum += get_vol(max_item)
sum += get_vol(array)

array[min_item[0]], array[max_item[0]] = max_item[1], min_item[1]
print(array)
print(f'{sum}')