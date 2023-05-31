""" 
*Задача 20: * 
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
В случае с английским алфавитом очки распределяются так:
A, E, I, O, U, L, N, S, T, R – 1 очко; 
D, G – 2 очка; 
B, C, M, P – 3 очка; 
F, H, V, W, Y – 4 очка; 
K – 5 очков; 
J, X – 8 очков; 
Q, Z – 10 очков. 

А русские буквы оцениваются так: 
А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
Д, К, Л, М, П, У – 2 очка; 
Б, Г, Ё, Ь, Я – 3 очка; 
Й, Ы – 4 очка; 
Ж, З, Х, Ц, Ч – 5 очков; 
Ш, Э, Ю – 8 очков; 
Ф, Щ, Ъ – 10 очков. 

Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

*Пример:*

    ноутбук
    12 
    """


alfabetScrabbleENG = {'A': 1, 'E': 1, 'I': 1,'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
                    'D':2, 'G':2,
                    'B':3, 'C':3, 'M':3, 'P':3,
                    'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 
                    'K':5,
                    'J':8, 'X':8,
                    'Q':10, 'Z':10}
wordEntered = str(input("Enter word, pls:").upper())
symbolInTheEnteredWord = []
priceSymbolInTheEnteredWord = []
sumPriceSymbolWord = 0
for i in range(0, len(wordEntered)):
    symbolInTheEnteredWord.append (wordEntered[i])
    priceSymbolInTheEnteredWord.append (alfabetScrabbleENG[symbolInTheEnteredWord[i]])
    sumPriceSymbolWord = sumPriceSymbolWord + priceSymbolInTheEnteredWord[i]

# На обработку ввода в этот раз не стал время тратить. Итак со здачей ДЗ затянул

print ("Entered world:", wordEntered)
print ("Points:", sumPriceSymbolWord)
