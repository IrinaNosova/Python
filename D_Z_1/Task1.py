# Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

num = int(input('Введите трехзначное число: '))
num3 = num % 10
num2 = (num // 10) % 10
num1 = num // 100
print(num1 + num2 + num3)