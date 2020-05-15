#varad parchure

from random import randint

l= ["rock", "paper", "scissors"]

comp= l[randint(0,2)]

player=False

while player==False:
    
    player=input("rock,paper,scissors\n")
    if player==comp:
        print("\n**** wow thats a tie ****")
    elif player== "rock" and comp=="paper":
        print("\n**** computer wins ****")
    elif player== "paper" and comp=="rock":
        print("\n**** player win ****")
    elif player== "scissors" and comp=="rock":
        print("\n**** computer smashed you ****")
    elif player== "rock" and comp=="scissors":
        print("\n**** you rocked and won ****")
    elif player== "paper" and comp=="scissors":
        print("\n**** computer wins ****")
    elif player== "scissors" and comp=="paper":
        print("\n**** player won ****")
    else:
        print("select a valid option only you idiot\n")
  
      
        print("\nCause computer had selected\n"+comp )
        print("*********************************************\n")
        
    player=False
    comp=l[randint(0,2)]        
        





