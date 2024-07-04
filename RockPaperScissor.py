"""
Work flow of Project:
1-Input from user(rock, Paper, Scissor)
2-Computer choice (computer will Choose)
3-Result print

Cases:
A- Rock
Rock-Rock = tie
Rock-Paper = Paper win
Rock-Scissor = Rock win

B- Paper
Paper-Paper = tie
Paper-Rock = Paper win
Paper-Scissor = Scissor win

C- Scissor
Scissor-Scissor = tie
Scissor-Paper = Scissor win
Scissor-Rock = Rock win
"""

import random
item_list = ["Rock", "Paper","Scissor"]
user_choice = input("Enter your move =")
computer_choice = random.choice(item_list)
 

print(f"User choice={user_choice},computer choice={computer_choice}")

if user_choice == computer_choice:
    print("Both chooses same : Match is Tie")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Computer Win")
    else:
        print("You Win")

elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Computer Win")
    else:
        print("You Win")
elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Computer Win")
    else:
        print("You Win")

