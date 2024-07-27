'''
SNAKE WATER GUN ---"FUNNY GAME"
1 for snake 
-1 for water 
0 for gun

'''
# random module to choice random number for computer 

import random   

computer = random.choice([-1,0,1])  
youstr = input("enter your choice :")
youDict = {"s":1, "w":-1,"g":0}      # enter your choice num from dict 
reverseDict={1: "Snake", -1: "Water" , 0: "Gun"}
you = youDict[youstr]

print(f" You choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}")

if(computer == you ):
    print(" Ohh no ,It's a Draw !! ")  # when comp and you choose the same num 

else:
    if(computer == -1 and you == 1):
        print("You Win !")

    elif(computer == -1 and you == 0):
        print(" You Lose ! ")

    elif(computer == 1 and you == -1):
        print("You Lose !")

    elif(computer == 1 and you == 0):
        print(" You Win !")

    elif(computer == 0 and you == -1):
        print(" You Win !")

    elif(computer == 0 and you == 1):
        print(" You Lose !")

    else:
        print("Something went Wrong !! ")
        print("Try Again :) ")    



