"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
 [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).

"""

import random as rnd


def bubble_sort(data):
    for i in range(len(data)):
        for k in range(len(data)-1):
            if data[k] < data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]


array = [rnd.randint(-100, 100) for _ in range(10)]
print(array)
bubble_sort(array)
print(array)
