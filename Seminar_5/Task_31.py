# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

"""
Решение через рекурсию
"""
# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# print(fib(int(input())))

"""
Решение с использованием словаря в декараторе и рекурсиии
"""


def memorize(func):
    d = {}

    def inner(num):
        if num not in d:
            d[num] = func(num)
        return d[num]
    return inner


@memorize
def fibonacci(n):
    """
    Возвращает n-ое число Фибоначчи
    """
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


for i in range(1, 20):
    print(i, fibonacci(i))
