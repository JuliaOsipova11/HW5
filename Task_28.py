# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций допускаются 
# только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4
 
A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))
def sum_of_numbers(A, B):
    if B == 0:
        return A
    return sum_of_numbers(A+1, B-1) 
print(sum_of_numbers(A, B))