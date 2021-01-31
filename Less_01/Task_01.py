"""
https://drive.google.com/file/d/1tPds4qxFhIehH94cWffSvXT6DC3JdCuP/view?usp=sharing

1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""

x = int(input("Введи положительное трехзначное число: "))

a = x // 100
b = x % 100 // 10
c = x % 10

s = a + b + c
m = a * b * c

print(f'Сумма цифр введенного числа = {s}')
print(f'Произведение цифр введенного числа = {m}')