"""
Задача 18: 
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

    5
    1 2 3 4 5
    6
    -> 5
"""

from random import randint

randomList = []
while True:
    try:
        listLenght = int(input("How many numbers (2 - 99)? :"))

        if (listLenght > 1) and (listLenght < 100):
            j = 0

            #create list with random numbers
            while (j < listLenght):
                randomList.append(randint(0, 99))
                j += 1

            while True:
                try:
                    numberForFind = int(input("Your number for find (0 - 99)? :"))
                    if (numberForFind >= 0) and (numberForFind < 100):
                        result = randomList[0]
                        diff = abs(numberForFind - randomList[0])
                        diffMin = 1000
                        for i in range(1, len(randomList)):
                            if (diffMin > abs(numberForFind - randomList[i]) ):
                                diffMin = abs(numberForFind - randomList[i])
                                result = randomList[i]
                        print (randomList)
                        print ("Your number for find:", numberForFind)
                        print ("Closest number", result)
                        break        
                    else:
                        print ("Enter number (0 - 99)")
                                    
                except:
                    print ("Invalid enter. Only numbers")

            break

        else:
            print ("Enter number (1 - 99)")
            
    except:
        print ("Invalid enter. Only numbers")

