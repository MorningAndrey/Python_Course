# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод:
# 1

import random
coins = list(range(int(input())))
for i in coins:
    coins[i] = random.randint(0, 1)
print(*coins)
if coins.count(0) > coins.count(1):
    print(coins.count(1))
else:
    print(coins.count(0))
