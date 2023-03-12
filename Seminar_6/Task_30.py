# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки

# pytest -v tests\test_30.py

quantity = int(input("Введите количество элементов прогрессии:\n"))
diff = int(input("Введите разность элементов прогрессии:\n"))
first = int(input("Введите первый элемент прогрессии:\n"))


def arithmetic_progression(first: int,
                           diff: int,
                           quantity: int) -> list[int]:
    """Возвращает список арифметической прогрессии по заданным:
    1) первый элемент
    2) разность
    3) количество элементов"""

    array = []
    for i in range(0, quantity):
        array.append(first)
        first += diff
    return array


print(arithmetic_progression(first, diff, quantity))