# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()


# # import collections
# a = "a a a b c a a d c d d"
# # print(dict(collections.Counter("a a a b c a a d c d d")))
# n = 0
# i = 0
# for a[i] in range(len(a)):
#     if a[i] == a.split():
#         n += 1
#         print(a.split())

def getStrWithCount(lst: list) -> str:
    res_list, res_str = [], ""
    for item in lst:
        res_str += f"{item} " if item not in res_list else f"{item}_{res_list.count(item)} "
        res_list.append(item)
    return res_str.rstrip()


lst = list(input("введите список через пробел\n").split())
print(getStrWithCount(lst))
