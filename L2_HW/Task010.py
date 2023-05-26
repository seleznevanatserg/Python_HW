"""
Задача 10: 
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
"""


from random import randint

# определяем количество монет в мешке 
bagWithCoins = []
bagSize = randint(0, 32)    
print ("У вас есть мешок с монетами. Сколько их там, вы не знаете. \nХотите его высыпать, чтобы подсчитать количество монет, \nа заодно количество выпавших орлов и решек?")

while True:
    
    try:
        answer = input("(Y/N)") 
        if (answer == "Y") or (answer == "y"):
            
            # высыпаем содержимое мешка 
            i = 0
            while (i < bagSize):
                bagWithCoins.append(randint(0, 1))
                i = i + 1
            print (bagWithCoins)
            countCoin = 0
            countEagle0 = 0
            countTails1 = 0

            # определяем количество монет с определённой стороной 
            for countCoin in range(len(bagWithCoins)):
                if bagWithCoins[countCoin] == 0:
                    countEagle0 += 1
                else:
                    countTails1 += 1
                countCoin += 1

            # обработка результата
            if (countCoin == 0):
                print ("Монет в мешке не оказалось. Сплошное наедалово...")
            if (countCoin != 0):
                print (countCoin,"монет оказалось в мешке")   
                print (countEagle0,"монет выпало орлом (0)")
                print (countTails1,"монет выпало решкой (1)")
                coinsForTurn = 0
                if (countEagle0 > countTails1):
                    coinsForTurn = countTails1
                elif (countEagle0 == countTails1):
                    coinsForTurn = countEagle0
                else:
                    coinsForTurn = countEagle0
                print (coinsForTurn,"монет надо перевернуть до одинакого состояния")
                break

        elif (answer == "N") or (answer == "n"):
            print ("Как хочешь...")
            break
        else:
            print("Четко скажи: Y - если ДА или N - если НЕТ")

    except:
        print ("Чего-чего? Напиши Y - если ДА или N - если НЕТ")





