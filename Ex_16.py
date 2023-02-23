#  Требуется вычислить, сколько раз встречается некоторое
#   число X в массиве A[1..N]. Пользователь в первой строке вводит
#  натуральное число N – количество элементов в массиве. В последующих
#   строках записаны N целых чисел Ai. Последняя строка содержит число X

lengthList = int(input('Введите кол-во элементов в массиве: '))
x = int(input(f'Введите число от 1 до {lengthList}: '))
list = []
count = 0
import random
for i in range(lengthList):
    list.append(random.randint(1, lengthList))
print(list)
for i in list:
    if i == x:
        count += 1
print(count)

