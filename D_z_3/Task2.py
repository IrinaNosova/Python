# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
#  Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
#  В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

arr = []
arrayLastDigit = int(input('Введите колличество элементов в массиве: '))
for i in range(arrayLastDigit):
    arr.append(i+1)
digit = int(input('Введите число: '))
difinitionTemp = 0
for i in range(arrayLastDigit):
    difinition = abs(arr[i]-digit)
    if difinition < difinitionTemp:
        target = i
    difinitionTemp=difinition
print('Самое ближайшее число массива', arr[target])
