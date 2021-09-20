#Number Guessing Game
#Date: 17-08-2021

from art import logo
import os
from random import randint

clear = lambda: os.system('cls')

def hard_game():
  for hard_chance in range(0,5):
    number_choice = int(input("\nEnter the number:\n"))
    if number_choice > random_number:
      print(f"Your number is too high. You have {4-hard_chance} chances remaining.")
    elif number_choice < random_number:
      print(f"Your number is too low. You have {4-hard_chance} chances remaining.")
    elif number_choice == random_number:
      print("\nCongrats. You have guessed it correctly.")
      break
  if hard_chance == 4:
    print(f"\nYou lose. The number was {random_number}.")
  print("--------------------------------------------------------------")
  return(input("\nType 'yes' if you want to play again otherwise type 'no'.\n"))

def easy_game():
  for easy_chance in range(0,10):
    number_choice = int(input("\nEnter the number:\n"))
    if number_choice > random_number:
      print(f"Your number is too high. You have {9-easy_chance} chances remaining.")
    elif number_choice < random_number:
      print(f"Your number is too low. You have {9-easy_chance} chances remaining.")
    elif number_choice == random_number:
      print("\nCongrats. You have guessed it correctly.")
      break
  if easy_chance == 9:
    print(f"\nYou lose. The number was {random_number}")
  print("--------------------------------------------------------------")
  return(input("\nType 'yes' if you want to play again otherwise type 'no'.\n"))

play_game = input("Type 'yes' if you are ready to play otherwise type 'no'.\n")
while play_game == 'yes':
  clear()
  print(logo)
  print("\nWelcome to the game.")
  print("You have to guess a number between 1 and 100.")
  choice = input("\nType 'easy' to play the easy level otherwise type 'hard':\n")
  random_number = randint(1,101)
  if choice == "easy":
    print("\nYou have 10 chances remaining to answer correctly.")
    play_game = easy_game()
  elif choice == "hard":
    print("\nYou have 5 chances remaining to answer correctly.")
    play_game = hard_game()
clear()
print("Come back soon.")