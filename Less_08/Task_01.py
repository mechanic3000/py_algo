"""

1. Определить количество различных подстрок с использованием хеш-функции. Задача: на вход функции дана строка,
требуется вернуть количество различных подстрок в этой строке.

Примечание: в сумму не включаем пустую строку и строку целиком.

"""
import hashlib as hl
import timeit

def substr_counter(string):
    k = 1  # количество символов в подстроке
    trash = set()
    len_string = len(string)
    while k < len_string:
        for i in range(0, len_string+1):
            # trash.add(string[i:i + k])
            # trash.add(hl.sha1(string[i:i + k].encode('utf-8')).hexdigest())
            trash.add(hash(string[i:i + k]))
        k += 1

    return len(trash)-1


a = "ababс"  # a b c ab ba bc aba bab abc abab babc  - 11
b = "abab"  # a b ab ba aba bab - 6
c = "abcdef"  # a b c d e f ab bc cd de ef abc bcd cde def abcd bcde cdef abcde bcdef - 20


print(substr_counter(a), timeit.timeit('substr_counter(a)', number=100, globals=globals()), sep="===")
print(substr_counter(b), timeit.timeit('substr_counter(b)', number=100, globals=globals()), sep="===")
print(substr_counter(c), timeit.timeit('substr_counter(c)', number=100, globals=globals()), sep="===")

# с хэш функцией sha1
# 11===0.0045081819999999995
# 6===0.0068941050000000045
# 20===0.007874210999999999

# без хэш функции
# 11===0.0013855940000000004
# 6===0.0008421090000000006
# 20===0.0022175169999999987

# с функцией hash()
# 11===0.0010026969999999968
# 6===0.0006147209999999986
# 20===0.0016023930000000006