# Требуется найти в массиве A[1..N] самый близкий по величине элемент 
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

lengthList = int(input('Введите кол-во элементов в массиве: '))
x = int(input(f'Введите число от 1 до {lengthList}: '))
list = []

import random
for i in range(lengthList):
    list.append(random.randint(1, lengthList))
print(list)

m = abs(x - list[0])
numb = list[0]
for i in range(1, len(list)):
    if m > abs(x - list[i]):
        numb = list[i]
        m = abs(x - list[i])
print(f'Ближайшее число в массиве - {numb}')