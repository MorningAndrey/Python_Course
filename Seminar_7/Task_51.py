# Задача 51:
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод:                                   
# values = [0, 2, 10, 6]                  
# if same_by(lambda x: x % 2, values):
#     print(‘same’)
# else:
#     print(‘different’)

# Вывод:
# same

def char(x):
    return x % 2


# char = lambda x: x % 2

def same_by(characteristic, objects):
    objects = set(map(characteristic, objects))
    if len(objects) == 1:
        return True
    return False


mass = [1, 2, 3, 4]
print(same_by(lambda x: x % 2, mass))