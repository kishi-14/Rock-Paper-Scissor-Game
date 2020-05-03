import random as rd
import time
# instructions to play this game is given bellow
print("Welcome to the game. \n You have 3 options to choose from Rock, Paper or Scissor \n For Rock Choose \"r\" \n" "For paper Choose \"p\" \n For Scissors, choose \"s\"")
#choice player likes to make
choice = input("Enter your choice:").upper()
if choice == "r":
     print("Player choosed Rock")
elif choice == "p":
     print("Player choosed Paper")
elif choice == "s":
     print("Player choosed Scissors")
else:
     print("NOT FOUND")
options = ["r","p","s"]
other_choice = rd.choice(options)
print("The option selected" + other_choice)
time.sleep(1)
#if player chooses "r"
if choice == "r":
    if other_choice == "p":
        print("YOU LOST")
    elif other_choice == "s":
        print("YOU WON")   
    else:
        print("TIE")   
#if player chooses "p"
if choice == "P":
    if other_choice == "s":
        print("YOU LOST")
    elif other_choice == "r":
        print("YOU WON")
    else:
        print("TIE")
#if player chooses Scissors or "s"
if choice == "s":
    if other_choice == "r":
         print("YOU LOST")
    elif other_choice == "p":
        print("YOU WON")
    else:
        print("TIE")
	


