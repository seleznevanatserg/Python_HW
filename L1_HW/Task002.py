"""
Задача 2: Найдите сумму цифр трехзначного числа.
*Пример:*
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) 
"""

"""Вариант без цикла, расчитаный на правильный (аккуратный) ввод пользователем числа от 0 до 999"""
userNumber = int(input ("Enter your three-digit number: "))
summ = userNumber%10
summ = summ + ((userNumber//10)%10)
summ = summ + ((userNumber//100)%10)
print (summ)



"""Вариант c циклом, с проверкой на правильный ввод числа от -999 до 999"""
userNumber = int(input ("Enter your three-digit number: "))
if (userNumber < -999 or userNumber > 999):
    while (userNumber < -999 or userNumber > 999):
        print ("You entered some wrong number")
        userNumber = int(input ("Enter a three-digit number, please: "))
print ("Yeee. You entered number: ",userNumber)

summ = 0
if (userNumber != 0):
    a = userNumber
    if (a < 0):
        a = a * (-1)
    while (a > 0):
        summ = summ + a % 10
        a = a // 10
print ("The sum of the digits in your number: ", summ)