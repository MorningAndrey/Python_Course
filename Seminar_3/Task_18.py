# Задача 18: Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве.
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5
from random import randint
n = int(input("Введите число N: "))
x = int(input('Введите число X: '))
lis = [randint(i+1, 100) for i in range(n)]


def value(lis, x):
    return min(lis, key=lambda lis_number: abs(x - abs(lis_number)))


print(f'{n}\n{lis}\n{x}\n{value(lis,x)}')
