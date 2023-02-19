# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

#-----Start Method----------------------
# Метод ввода целого трехзначного числа с обработкой некорректного ввода
def correct_int() -> int:  
    is_correct = True
    while is_correct:
        a = input('Введите любое трехзначное число: ')
        try:
            a = int(a)
            if a >= 100 and a < 1000:
                is_correct = False
                return a
            else:
                print('Некорректный ввод. Необходимо ввести ТРЕХЗНАЧНОЕ число!')
        except ValueError:
            print('Некорректный ввод')
#-----End Method------------------------        
s = correct_int()
a = s // 100
b = s % 100 // 10
c = s % 10
sum = a + b + c
print(f'{s} -> {sum} ({a}+{b}+{c})')
