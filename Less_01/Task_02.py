"""

https://drive.google.com/file/d/1Yw-IuI0DzV7tFNoegJVOXjy1Kyosz7oD/view?usp=sharing

2.Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
вправо и влево на два знака.

"""

a = 5
b = 6

a_nd = a & b
o_r = a ^ b
in_a = ~a
in_b = ~b

five_l = a << 2
five_r = a >> 2

print(f"Результат операции AND - {a_nd}")
print(f"Результат операции OR - {o_r}")
print(f"Результат операции инверсия числа 5 - {in_a}")
print(f"Результат операции инверсия числа 6 - {in_b}")
print(f"Результат операции сдвиг влево на 2 числа 5 - {five_l}")
print(f"Результат операции сдвиг вправо на 2 числа 5 - {five_r}")