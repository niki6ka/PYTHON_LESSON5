"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""
a = int(input("Please enter A number: "))
b = int(input("Please enter B number: "))
def Rez_summ(a, b):
    return a if b == 0 else Rez_summ(a+1, b-1) if b > 0 else Rez_summ(a-1, b+1)

print("The result of adding the numbers A and B is: ", Rez_summ(a, b))