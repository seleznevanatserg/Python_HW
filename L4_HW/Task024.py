""" 
Задача 24: 
В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, 
которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки. 
"""

from random import randint

randomList = []

while True:
    try:
        #create bashes with bluberry
        listLenght = int(input("How many bushes of blueberry (3 - 19)? :"))
        if (listLenght > 2) and (listLenght < 20):
           
            #create bluberry on bush
            for i in range(0, listLenght):
                randomList.append(randint(1, 999))

            
            print ("Your bushes blueberry:", randomList)
            gatherSuccessfull = []
            gather = ()
            maxGatherSum = 0
            
            #variant harvesting
            for i in range(0, len(randomList)):
                if (i == 0):
                    bush = i
                    bushR = i + 1
                    bushL = len(randomList)-1
                elif (i == len(randomList) - 1):
                    bush = len(randomList)-1
                    bushR = 0
                    bushL = len(randomList)-2
                else:
                    bush = i
                    bushR = i + 1
                    bushL = i - 1
                
                gatherSum = randomList[bush] + randomList[bushR] + randomList[bushL]
                gather = (gatherSum, bushL, bush, bushR)

                if (maxGatherSum <= gatherSum):
                    maxGatherSum = gatherSum
                    
                gatherSuccessfull.append(gather)
                
            print ("Harvest Options:", gatherSuccessfull)
            print ("Max Harvesting:", maxGatherSum)
         
            break
        else:
            print ("Enter number (3 - 19)")
    except:
        print ("Invalid enter. Only numbers")
