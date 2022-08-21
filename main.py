import random 

counter_user=0
counter_pc=0

liste=["rock","paper","scissors"]   

print("""
Welcome to the Rock-Paper-Scissors game.
Rules are pretty the same, Rock crushes Scissors, Paper covers Rock & Scissors cuts Paper.

Please enter your choice
!! press q to exit\n""")

while True:
    user=input("User  :  ").lower()
    a =random.choice(liste)
    if user == "rock":
        if a=="rock" :
            print("PC    :  rock")
            print("No Winner\n")
        elif a=="paper" :
            print("PC    :  paper")
            print("Paper covers Rock..\n" )
            counter_pc += 1
        elif a== "scissors":
            print("PC    :  scissors")
            print("Rock crushes Scissors..\n")   
            counter_user += 1 

    elif user == "paper":
        if a=="rock" :
             print("PC    :  rock")
             print("Paper covers Rock..\n" )   
             counter_user += 1         
        elif a=="paper" :
            print("PC    :  paper")
            print("No Winner\n")
        elif a== "scissors":
            print("PC    :  scissors")
            print("Scissors cuts Paper..\n") 
            counter_pc += 1

    elif user == "scissors":
        if a=="Rock" :
             print("PC    :  rock")
             print("Rock crushes Scissors..\n")    
             counter_pc += 1      
        elif a=="paper" :
             print("PC    :  paper")
             print("Scissors cuts Paper..\n") 
             counter_user += 1
        elif a == "scissors":  
             print("PC    :  scissors") 
             print("No Winner\n")       
    else:
        print("incorrect entry!!\n")

    if user == "q":
        print("Game Over")
        break
print(f"User: {counter_user}  ,  Pc: {counter_pc} ")
if counter_user > counter_pc:
    print("Winner  **USER** ")
elif counter_pc > counter_user:
    print("Winner  **PC** ")
else:
    print("Equal Score")
