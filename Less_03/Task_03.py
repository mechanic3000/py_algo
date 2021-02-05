"""
3 В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_item = [0, MAX_ITEM]
max_item = [0, 0]

for i, item in enumerate(array):
    if item < min_item[1]:
        min_item[0], min_item[1] = i, item
    elif item > max_item[1]:
        max_item[0], max_item[1] = i, item

array[min_item[0]], array[max_item[0]] = max_item[1], min_item[1]
print(array)