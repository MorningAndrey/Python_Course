# Задача 45. Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна
# числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое
# из которых не превосходит k. Программа получает на вход одно натуральное
# число k, не превосходящее 10^5. Программа должна вывести
# все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами.
# Каждая пара должна быть выведена только один раз
# (перестановка чисел новую пару не дает).

# 220 -> sum(1, 2, 4, 5, 10, 11, 20, 22, 44, 55,  110 ) = 284
# 284 -> sum(1, 2, 4, 71,  142) = 220


def get_divider_list(number: int) -> list:
    div_list = list()
    for i in range(1, number):
        if number % i == 0:
            div_list.append(i)
    return div_list


def get_friendly_pairs(border_number: int) -> dict:
    friendly_num_dict = dict()
    for num_1 in range(1, border_number + 1):
        num_2 = sum(get_divider_list(num_1))
        if (sum(get_divider_list(num_2)) == num_1 and
            num_1 != num_2 and
            num_2 not in friendly_num_dict and
                num_2 < border_number):
            friendly_num_dict[num_1] = num_2
    return friendly_num_dict


def print_friendly_pairs(output_dict: dict):
    for key in output_dict:
        print(f'{key} {output_dict[key]}')


k = int(input('Введите K: '))
result_dict = get_friendly_pairs(k)
print_friendly_pairs(result_dict)
