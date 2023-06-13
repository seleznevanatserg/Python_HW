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

def selectAllReadPhoneNumber ():
    phoneBook = readData('C:/1Stud_GB/PythonLessons/L8/phonebook.txt')
    for i in phoneBook:
        print (i)
def selectSomethingReadPhoneNumber ():
    print ("selectSomething 2")

def readData (fileName):
    with open(fileName) as f:
        phoneBook = []
        for line in f:
            phoneBook.append(line.split(','))
    return phoneBook

def writeData (fileName, phoneBook):
    with open(fileName) as f:
        f.writelines(phoneBook) 
        print ("Data added and saved")

def addPerson (phoneBook):
    print ("Entered data:")
    number = max(len(phoneBook) + 1)
    surname = str(input("Entered surname:"))
    nameFirst = str(input("Entered first name:"))
    nameSecond = str(input("Entered second name:"))
    phoneNumber = int(input("Entered telephone number:"))
    phoneBook.append([number, surname, nameFirst, nameSecond, phoneNumber])
    writeData('C:/1Stud_GB/PythonLessons/L8/phonebook.txt', phoneBook)


print ('''HELLO, USER 
        \n [1] -- press for SHOW ALL 
        \n [2] -- press for SELECT 
        \n [3] -- press for ADD DATA''')
while True:
    try:
        if (int(input()) == 1):
            selectAllReadPhoneNumber()
        elif (int(input()) == 2):
            selectSomethingReadPhoneNumber()
        elif (int(input()) == 3):
            addPerson (readData)    
        else:
            print("Your number out of range. Try again")
            break
    except:
        print ("You entered something, but it's not number")




