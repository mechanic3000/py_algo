"""
https://drive.google.com/file/d/1T3evDioIsGRfoh7PKoqOJ2ckr9y3N1te/view?usp=sharing

6.Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

"""

n = int(input("Введи поряднковый номер буквы русского алфавита: "))+1071

if n > 1077:
    if n == 1078:
        letter = "ё"
    else:
        letter = chr(n-1)
else:
    letter = chr(n)

print(f"Вы ввели номер буквы {letter}")
