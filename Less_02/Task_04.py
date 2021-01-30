"""

https://drive.google.com/file/d/13zb4J4pyd7ZlVS8u1I6YyuAy21Az0YHc/view?usp=sharing

4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… Количество элементов (n) вводится
с клавиатуры.

"""

def magic_summ(n) -> float:
    s = 1 * (1 - 0.5 ** n) / (1 - 0.5)
    return s


n = int(input("Ввведи количество элементов: "))
z = magic_summ(n)
print(z)
