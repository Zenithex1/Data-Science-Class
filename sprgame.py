import random

spr = ["ROCK","SCISSORS","PAPER"]


# while True:
#     comp_choice = random.choice(spr)
#     user_choice = (input("Enter your choice(Scissors,Paper,Rock): ")).upper()
#     if user_choice == "SCISSORS" or user_choice == "PAPER" or user_choice == "ROCK" :
#         while comp_choice == "SCISSORS":
#                 if user_choice == "ROCK":
#                     print(f'Computer chose: {comp_choice}')
#                     print("You won the match")
#                 elif user_choice == "PAPER":
#                     print(f'Computer chose: {comp_choice}')
#                     print("You lost the match")
#                 else:
#                     print(f'Computer chose: {comp_choice}')
#                     print("Draw")
#                 break
#         while comp_choice == "ROCK":
#                 if user_choice == "PAPER":
#                     print(f'Computer chose: {comp_choice}')
#                     print("You won the match")
#                 elif user_choice == "SCISSORS":
#                     print(f'Computer chose: {comp_choice}')
#                     print("You lost the match")
#                 else:
#                     print(f'Computer chose: {comp_choice}')
#                     print("Draw")
#                 break
#         while comp_choice == "PAPER":
#                 if user_choice == "SCISSORS":
#                     print(f'Computer chose: {comp_choice}')
#                     print("You won the match")
#                 elif user_choice == "ROCK":
#                     print(f'Computer chose: {comp_choice}')
#                     print("You lost the match")
#                 else:
#                     print(f'Computer chose: {comp_choice}')
#                     print("Draw")
#                 break      
#     else:
#         print("Your input is incorrect")


spr = ["ROCK","SCISSORS","PAPER"]
count = 5
while True:
    comp_choice = random.choice(spr)
    if count> 0:
             count -=1
    else:
            again  = input("Do you want to play again (Y/N): ").upper()
            if again != 'Y':
             break
            else:
                 count = 5
    user = input(("Enter your choice (Scissor,Paper,Rock) : ")).upper()
    if user not in spr:
        print("Wrong input ")
        continue
    elif user == comp_choice:
        print("Draw")
        
    elif (comp_choice == "ROCK" and user =="PAPER") or (comp_choice == "PAPER" and user =="SCISSORS") or (comp_choice == "SCISSORS" and user == "ROCK"):
        print(f"Computer chose:{comp_choice}")
        print("You won the match")
    else:   
        print(f"Computer chose:{comp_choice}")
        print(f"You lose the match")
       
        