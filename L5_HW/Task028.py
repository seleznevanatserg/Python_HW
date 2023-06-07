""" Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4  """



def sumAB(numA, numB):
    if (numB == 0):
        return numA
    else:
        return sumAB(numA + 1, numB - 1)
a = int(input("Enter number A:"))
b = int(input("Enter number B:"))
print (sumAB(a,b))
