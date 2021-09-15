#Rock, Paper, Scissor game
import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to the rock, paper and scissors contest!!")

item = [rock, paper, scissors]
user_choice = int(input("\nWhat do you want to choose?\nType 1 for \033[1mRock\033[0m\nType 2 for \033[1mPaper\033[0m\nType 3 for \033[1mScissor\033[0m\n"))

computer_choice = random.randint(1,3)
if user_choice == computer_choice:
  print(f"Computer choice:\n{item[computer_choice-1]}\n")
  print(f"Your choice:\n{item[user_choice-1]}\n")
  print("Its a tie.\n")

elif (computer_choice == 1 and user_choice == 3) or (computer_choice == 2 and user_choice == 1) or (computer_choice == 3 and user_choice == 2) :
  print(f"Computer choice:\n{item[computer_choice-1]}\n")
  print(f"Your choice:\n{item[user_choice-1]}\n")
  print("You lose.\n")

elif (computer_choice == 3 and user_choice == 1) or (computer_choice == 1 and user_choice == 2) or (computer_choice == 2 and user_choice == 3) :
  print(f"Computer choice:\n{item[computer_choice-1]}\n")
  print(f"Your choice:\n{item[user_choice-1]}\n")
  print("You Win. Congrats.\n")

else:
  print("Please enter valid number.\n")
