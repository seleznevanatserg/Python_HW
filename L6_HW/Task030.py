""" 
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки. 
"""
result = []
print ("We have next formula: An = A1 + (n-1)*d")
a = int(input("Enter first number (A1):"))
n = int(input("Enter amount numbers (n):"))
d = int(input("Enter difference (d):"))

i = 1
while (i < n+1):
    result.append(a + (i-1)*d)
    i += 1
print (result)