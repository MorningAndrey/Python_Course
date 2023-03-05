# '35. 1. Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым

# *Напоминание: Простое число - это число, которое имеет 2 делителя:
# 1  и n(само число)*


n = int(input())


def natural(int: n) -> int:
    result = [1 for i in range(2, n + 1) if n % i == 0]
    if len(result) == 1:
        print('Yes')
    else:
        print('No')


natural(n)
