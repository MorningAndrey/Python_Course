# 19. Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на
# k = 4
# print(r[:-1] + r[:k])

n = int(input())
k = 4
sequence = [i+1 for i in range(n)]

for i in range(k):
    sequence.insert(0, sequence.pop())
    print(sequence)
