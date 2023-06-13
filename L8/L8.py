""" 
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи (Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной 
"""

# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines() # разделителей не будет
# data.close()

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
# print(line)
# data.close()
import os
def selectAllReadPhoneNumber ():
    phoneBook = readData('C:/1Stud_GB/PythonLessons/L8/phonebook.txt')
    for i in phoneBook:
        print (i)
def selectSomethingReadPhoneNumber ():
    print ("selectSomething 2")

def readData (fileName):
    with open (fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(','))
    return phoneBook

def writeData (fileName, phoneBook):
    with open (fileName, 'w') as f:
        for i in phoneBook:
            print (i)
            f.write (','.join(i))
            
        print ("Data added and saved")

def addPerson ():
    phoneBook = readData('C:/1Stud_GB/PythonLessons/L8/phonebook.txt')
    print ("Entered data:")
    number = str(len(phoneBook) + 1)
    surname = str(input("Entered surname:"))
    nameFirst = str(input("Entered first name:"))
    nameSecond = str(input("Entered second name:"))
    phoneNumber = str(input("Entered telephone number:"))
    phoneBook.append([number, surname, nameFirst, nameSecond, phoneNumber])
    print (phoneBook)
    writeData('C:/1Stud_GB/PythonLessons/L8/phonebook.txt', phoneBook)

clear = lambda: os.system ('cls')
clear()

print ('''HELLO, USER 
        \n [1] -- press for SHOW ALL 
        \n [2] -- press for SELECT 
        \n [3] -- press for ADD DATA''')
while True:

    enteredNum = int(input())
    # try:
    if (enteredNum == 1):
        selectAllReadPhoneNumber()
    elif (enteredNum == 2):
        selectSomethingReadPhoneNumber()
        phoneBook = readData('C:/1Stud_GB/PythonLessons/L8/phonebook.txt')
        phoneBook.append(['5', 'H', 'R', 'T', '123\n'])
        writeData ('C:/1Stud_GB/PythonLessons/L8/phonebook.txt', phoneBook)
    elif (enteredNum == 3):
        addPerson ()    
    else:
        print("Your number out of range. Try again")
        break
    # except:
    #     print ("You entered something, but it's not number")




