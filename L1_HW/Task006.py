"""
Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

*Пример:*
385916 -> yes
123456 -> no
"""

userNumber = int(input ("Enter your six-digit number (000000 - 999999): "))
if (userNumber < 0 or userNumber > 999999):
    while (userNumber < 0 or userNumber > 999999):
        print ("You entered some wrong number")
        userNumber = int(input ("Enter a six-digit number, please: "))
print ("Yeee. You entered number: ",userNumber)

sumLeftHalfNumber = 0
if (userNumber//1000 != 0):
    a = userNumber//1000
    while (a > 0):
        sumLeftHalfNumber = sumLeftHalfNumber + a % 10
        a = a // 10

sumRightHalfNumber = 0
if (userNumber%1000 != 0):
    a = userNumber%1000
    while (a > 0):
        sumRightHalfNumber = sumRightHalfNumber + a % 10
        a = a // 10
if (sumLeftHalfNumber == sumRightHalfNumber):
    print ("Yeee. You entered luck ticket`s number: ",userNumber)
else:
    print ("Sorry. You entered odrdinary ticket`s number: ",userNumber)