# Задача 6:
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

import random
num = random.randint(100000, 1000000)
print(f'{num} -> ', end='')
number = str(num)
l = int(number[:3])
r = int(number[3:])
#-----Start Method----------------------
# Метод определения суммы трехзначного числа
def sum(s):
    a = s // 100
    b = s % 100 // 10
    c = s % 10
    sum = a + b + c
    return sum
#-----End Method----------------------
if sum(l) == sum(r):
    print('yes')
else:
    print('no')
