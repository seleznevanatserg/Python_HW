""" 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств. 
"""
from random import randint

randomListN = []
randomListM = []

while True:
    try:
        listLenghtN = int(input("Number N (1 - 19)? :"))
        if (listLenghtN > 0) and (listLenghtN < 20):
            for i in range(0, listLenghtN):
                randomListN.append(randint(0,100))
        else:
            print ("Enter number N (1 - 19)")
        listLenghtM = int(input("Number M (1 - 19)? :"))
        if (listLenghtM > 0) and (listLenghtM < 20):
            for i in range(0, listLenghtM):
                randomListM.append(randint(0,100))
        else:
            print ("Enter number M (1 - 19)")
        
        randomListN = sorted(randomListN)
        randomListM = sorted(randomListM)
        
        arraysOrMN = []
        j = 0
        if (max(randomListN) >= max(randomListM)):
            j = max(randomListN)
        else:
            j = max(randomListM)


        print (randomListN)
        print (randomListM)



    except:
        print ("Invalid enter. Only numbers")

