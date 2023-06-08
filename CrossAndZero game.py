""" 
0	1	2
3	4	5
6	7	8
0	3	6
1	4	7
2	5	8
0	4	8
3	4	6
"""
#field for game
field = [0, 1, 2, 3, 4, 5, 6, 7, 8]

#printed field
def fieldPrint(field):
    print (field[0]," ",field[1]," ",field[2])
    print (field[3]," ",field[4]," ",field[5])
    print (field[6]," ",field[7]," ",field[8])

#cheking winner
def checkWinCombination(field):
    if (field[0] == field[1] == field[2]) or (field[3] == field[4] == field[5]) or (field[6] == field[7] == field[8]) or (field[0] == field[3] == field[6]) or (field[1] == field[4] == field[7]) or (field[2] == field[5] == field[8]) or (field[0] == field[4] == field[8]) or (field[2] == field[4] == field[6]):
        return True
    else:
        return False

#player change
def messageOfRound(indexP):
    if (indexP == 0):
        print ("You GO, human")
    elif (indexP == 1):
        print ("Comp GO")
    else:
        print ("ERROR: Number players")


fieldPrint(field)

count = 0
win = False
players = ['HUMAN', 'COMP']
while (win == False):
        
    messageOfRound(count % 2)
    print ("Round:", count + 1) 

    if (count % 2 == 0):
        while True:
            try:
                print ("Enter number of free cell (0-8)")
                target = int(input())
                if (target >= 0) and (target <= 8):
                    if (field[target] != "X") and (field[target] != "O"):
                        field[target] = "X"
                        break
                    else:
                        print ("Cell is occupied")
                else:
                    print ("Out of range")
            except:
                print ("Its not number")
    elif(count % 2 == 1):
        for i in range(0, 8):
            if (field[i] != "X") and (field[i] != "O"):
                field[i] = "O"
                break
    else:
        print ("ERROR: playing players")
    
    fieldPrint(field)
    print ()

    if (count >= 4):
        win = checkWinCombination(field)
        if (win == True):
            print ("player", players[count % 2], "win!")
            break
    else:
        count += 1

    if (count == len(field)):
        print ("YEEE! NOT WINNERS! ALL LOSERS!... Oops, sorry, wrong line. \nFRIENDSHIP WIN! :3 ")
        break
    



