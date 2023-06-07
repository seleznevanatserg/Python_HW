""" Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8  """


def degreeAB(numA, numB):
    if (numB == 0):
        return 1
    return numA * degreeAB(numA, numB - 1)

a = int(input("Enter number A:"))
b = int(input("Enter number B:"))
print (degreeAB (a, b))