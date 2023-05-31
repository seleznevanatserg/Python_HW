"""
Задача 16: 
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

*Пример:*

5
1 2 3 4 5
3
-> 1
"""
from random import randint

numberSet = []

while True:
    
    try:
        listLenght = int(input("How many numbers (1 - 99)? :"))

        if (listLenght > 0) and (listLenght < 100):
            i = 0

            #create list with random numbers
            while (i < listLenght):
                numberSet.append(randint(0, 9))
                i = i + 1

            try:
                numberForFind = int(input("Your number for find (0 - 9)? :"))
                if (numberForFind >= 0) and (numberForFind < 10):
                    i = 0

                    #quantity counter entered number
                    count = 0
                    while (i < listLenght):
                        if (numberForFind == numberSet[i]):
                            count += 1
                        i += 1
                    
                    print ("Your list of numbers")
                    print (numberSet)
                    print ("Your entered number:", numberForFind)
                    print ("Quantity number list of numbers:", count)
                    break
                else :
                    print ("Enter number (0 - 9)")
                    
            except:
                print ("Invalid enter. Only numbers")        
            

        else :
            print ("Enter number (1 - 99)")
        
    except:
        print ("Invalid enter. Only numbers")