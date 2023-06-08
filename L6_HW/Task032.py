""" 
Задача 32: 
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)

 """
from random import randint

randomList = []
def randomListInt(listR = []):
    lenght = randint(5,20)
    for i in range(0, lenght):
        listR.append (randint(-99,99))
    return listR
print (randomListInt(randomList))

leftLimit = int(input("Enter left range limit (not included):"))
rightLimit = int(input("Enter right range limit (not included):"))

# checking options not setup

result = []
res = ()
countNum = 0 
for i in range(0, len(randomList)):
    if (randomList[i] > leftLimit) and (randomList[i] < rightLimit):
        res = (randomList[i], i)
        result.append(res)
        countNum += 1
if (countNum == 0):
    result.append("Dont have numbers in entered range")
print ("Number, index", result)

