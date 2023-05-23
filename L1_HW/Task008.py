"""
Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить ровно k долек, 
если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*
3 2 4 -> yes
3 2 1 -> no
"""

nLong = int(input ("Enter your number for N (1 - 9): "))
if (nLong < 1 or nLong > 9):
    while (nLong < 1 or nLong > 9):
        print ("You entered some wrong number")
        nLong = int(input ("Enter number for N, please: "))
print ("Yeee. You entered number: ",nLong)

mWidth = int(input ("Enter your number for M (1 - 9): "))
if (mWidth < 1 or mWidth > 9):
    while (mWidth < 1 or mWidth > 9):
        print ("You entered some wrong number")
        mWidth = int(input ("Enter number for M, please: "))
print ("Yeee. You entered number: ",mWidth)

kParts = int(input ("Enter your number for K (how many you will break parts a chocolate bar): "))
if (kParts < 1 or kParts > nLong*mWidth):
    while (kParts < 1):
        print ("Negative number of chunks? Funny.")
        kParts = int(input ("Enter number for K, please: "))
    while (kParts > nLong*mWidth):
        print ("You dont have so many parts a chocolate bar")
        kParts = int(input ("Enter number for K, please: "))
    while (kParts == 0):
        print ("Are You will eating chocolate bar entirely?")
        kParts = int(input ("Maybe break off a piece?.. "))
if (kParts >= 1 or kParts <= 9):
    while (kParts == nLong*mWidth):
        print ("Don't need a breaking. But are You will eating chocolate bar entirely?")
        kParts = int(input ("Maybe break off a piece?.. "))
    if ((kParts % nLong != 0) or (kParts % mWidth != 0)):
        print ("A You managed to break off a few pieces:", kParts)
    else:
        print ("You failed to break off a few pieces.")
   
