# 23. Дан массив, состоящий из целых чисел. Напишите программу, которая
# подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером)
# 1 2 3 4 3 2 1 -> 3 (2 , 3 , 4)

lis = [0, -1, 5, 6, 5]
count = 0
for i in range(1, len(lis)):
    if lis[i-1] < lis[i]:
        count += 1
print(count)