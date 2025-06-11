#We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user.
import random

'''
1 for stone
-1 for paper
0 for scissors
'''


computer=random.choice([-1,1,0])
youstr=input("Enter your choice : ")
youDict={"s":1,"p":-1,"sc":0}
reverseDict={1:"Stone",-1:"Paper",0:"Scissors"}

you=youDict[youstr]

print(f"You chose {reverseDict[you]}\n Computer chose {reverseDict[computer]}")

if(computer==you):
    print("Its a draw")
else:
    if(computer==-1 and you==1):
        print("You loose!!")
    elif(computer==-1 and you==0):
        print("You win!!")
    elif(computer==1 and you==-1):
        print("You win!!")
    elif(computer==1 and you==0):
        print("You loose!!")
    elif(computer==0 and you==-1):
        print("You loose!!")
    elif(computer==0 and you==1):
        print("You win!!")
    else:
        print("Something went wrong!!")