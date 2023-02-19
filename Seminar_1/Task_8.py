# Задача 8:
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

# -----Start Method----------------------
# Ввод целого числа с обработкой некорректного
def correct_int() -> int:
    is_correct = True
    while is_correct:
        a = input('Введите любое число: ')
        try:
            a = int(a)
            is_correct = False
            return a
        except ValueError:
            print('Некорректный ввод')
# -----End Method----------------------


n = correct_int()
m = correct_int()
k = correct_int()
print(f'{n} {m} {k} -> ', end ='')
if k <= n * m and ((k % n == 0) or (k % m == 0)):
    print('yes')
else:
    print('no')
