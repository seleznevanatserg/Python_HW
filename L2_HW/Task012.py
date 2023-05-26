"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.

"""

from random import randint
num1 = randint(1, 1000) 
num2 = randint(1, 1000)
print (num1, num2)

sumNum1Num2 = num1 + num2
prodNum1Num2 = num1 * num2
print ("Сумма двух загаданных чисел:", sumNum1Num2)
print ("Произведение двух загаданных чисел:", prodNum1Num2)

for num1Answer in range (1, 1000):
    for num2Answer in range (1, 1000):
        if (num1Answer + num2Answer == sumNum1Num2) and (num1Answer * num2Answer == prodNum1Num2):
            print ("загаданные числа", num1Answer, num2Answer)

