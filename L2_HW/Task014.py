"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

"""

while True:
    
    try:
        num = int(input("Enter your number (0 - 99999)"))
        if (num >= 0) and (num < 10000):
            degree = 0
            result = 0
            nDegreeK = []

            while (result <= num):
                result = 2 ** degree
                nDegreeK.append(result)
                degree += 1
            nDegreeK.pop(degree-1)

            print (nDegreeK)
            break

        else:
            print("Your number out of range. Try again")

    except:
        print ("You entered something, but it's not number")

