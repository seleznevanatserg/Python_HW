"""
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, 
что Петя и Сережа сделали одинаковое количество журавликов, 
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
60 -> 10  40  10 
"""

"""Вариант c циклом, с проверкой на правильный ввод числа от -999 до 999"""
userNumber = int(input ("На столе лежа бумажные журавли. Сколько их там (число от 0 до 1000): "))
if (userNumber < 0 or userNumber > 1001):
    while (userNumber < 0 or userNumber > 1001):
        print ("Что-то не то...")
        userNumber = int(input ("Вы пересчитали журавликов и получили следующую цифру: "))
print ("Да, на столе", userNumber, "журавликов")
peter = 1
sergey = 1
kate = 4
count = 0
summ = 0

while (summ <= userNumber):
    count = count + 1
    summ = (peter + sergey + kate)*count  
    
count = count - 1
summ = (peter + sergey + kate)*count  

print ("Журавликов сделали дети: Петя -- ", peter*count,", Серёжа --",sergey*count ,"и Катя --",kate*count)
print ("И", userNumber-summ, "сделали неизвестные. Но это совсем другая история... (с) ")
