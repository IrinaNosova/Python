# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность
# и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1=int(input('Введите первый элемент множиства: '))
d=int(input('Введите разность: '))
n=int(input('Введите колличество элементов: '))
list1=[]
for i in range (1,n+1):
    list1.append(a1+(i-1)*d)
print(list1)