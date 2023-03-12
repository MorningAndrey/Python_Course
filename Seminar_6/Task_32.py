# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# pytest -v tests\test_32.py


def is_in_mass(num_lst: list[int],
               min_num: int,
               max_num: int) -> list[int]:
    """Возвращает список индексов элементов списка, которые
    находятся в диапазоне [min_num,max_num] """
    array = []
    for i in range(len(num_lst)):
        if min_num <= num_lst[i] <= max_num:
            array.append(i)
    return array


min_num = int(input("Введите минимум для заданного диапазона:\n"))
max_num = int(input("Введите максимум для заданного диапазона:\n"))
num_lst = list(map(int, input("Введите числа через пробел: ").split()))
print(is_in_mass(num_lst, min_num, max_num))
