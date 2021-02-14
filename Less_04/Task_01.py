import timeit
# import cProfile
import random


"""
поменять местами макс и мин

"""

# def some_func(n):
#     SIZE = n
#     MIN_ITEM = 0
#     MAX_ITEM = 100
#     array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#     # print(array)
#
#     for i, item in enumerate(array):
#         try:
#             if item < min_item[1]:
#                 min_item[0], min_item[1] = i, item
#         except NameError:
#             min_item = [i, item]
#
#         try:
#             if item > max_item[1]:
#                 max_item[0], max_item[1] = i, item
#         except NameError:
#             max_item = [i, item]
#
#     array[min_item[0]], array[max_item[0]] = max_item[1], min_item[1]
#
#
# print(timeit.timeit('some_func(10)', number=100, globals=globals()))            #0.004768765000000001
# print(timeit.timeit('some_func(100)', number=100, globals=globals()))           #0.035210964000000004
# print(timeit.timeit('some_func(1_000)', number=100, globals=globals()))         #0.18313514400000003
# print(timeit.timeit('some_func(10_000)', number=100, globals=globals()))        #1.9813432179999997

# def some_func(n):
#     SIZE = n
#     MIN_ITEM = 0
#     MAX_ITEM = 100
#     array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
#     # print(array)
#
#     max_item = max(array)
#     max_item_pos = array.index(max_item)
#     min_item = min(array)
#     min_item_pos = array.index(min_item)
#
#     array[min_item_pos], array[max_item_pos] = max_item, min_item
#
#
#
# print(timeit.timeit('some_func(10)', number=100, globals=globals()))            #0.002744767000000002
# print(timeit.timeit('some_func(100)', number=100, globals=globals()))           #0.026938366999999998
# print(timeit.timeit('some_func(1_000)', number=100, globals=globals()))         #0.0.19373289100000002
# print(timeit.timeit('some_func(10_000)', number=100, globals=globals()))        #1.545190415