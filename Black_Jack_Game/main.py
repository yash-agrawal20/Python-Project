############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##############################################################

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
#Date: 16-08-2021

from art import logo
import random
import os

clear = lambda: os.system('cls')

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []
decision = input("Are you ready to play the Blackjack game? Type 'yes' to continue otherwise type 'no'.\n")
clear()

while decision == 'yes':
  print(logo)

  user_cards.append(random.choice(cards))
  user_cards.append(random.choice(cards))
  user_sum = sum(user_cards)

  computer_cards.append(random.choice(cards))
  computer_sum = sum(computer_cards)
  
  print(f"\nYour cards: {user_cards}")
  print(f"\nComputer cards: {computer_cards}")
  decision2 = 'hit'
  
  while user_sum < 21 and computer_sum < 21 and decision2 == "hit":
    decision2 = input("\nType 'hit' if you want a card, for standing type 'wait'.\n")
    if user_sum > 10 or computer_sum > 10:
      cards[0] = 1

    if decision2 == 'hit':
      user_cards.append(random.choice(cards))
      user_sum = sum(user_cards)
      print(f"\nYour cards: {user_cards}")
    elif decision2 == 'wait':
      computer_cards.append(random.choice(cards))
      computer_sum = sum(computer_cards)
      while computer_sum < 17:
        computer_cards.append(random.choice(cards))
        computer_sum = sum(computer_cards)
      print(f"\nComputer cards: {computer_cards}")
    

  if user_sum == 21:
    print("\nYou win. Congrats.")
  elif user_sum > 21:
    print("\nYou have exceeded the limit. You lose.")
  elif computer_sum > 21:
    print("\nComputer has exceeded the limit. You Win.")
  elif computer_sum == user_sum:
    print("\nDraw")
  elif computer_sum > user_sum:
    print("\nComputer wins.")
  elif computer_sum < user_sum:
    print("\nYou win. Congrats.") 
  print("-------------------------------------------------------")
  
  user_cards.clear()
  computer_cards.clear()

  decision = input("\nGood Game. If you want to play again type 'yes' otherwise 'no'\n")
  clear()
  if decision == "no":
    print("\nCome back soon.") 

