"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8

"""
a = int(input("Please enter A number: "))
b = int(input("Please enter B number: "))
def expo (a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * expo(a, b - 1))

print("The result of raising the number A to the power of B is: ", expo(a, b))


