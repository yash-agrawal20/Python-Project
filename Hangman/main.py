#Hangman game
#Date: 13-08-2021
import os #For clear command
import random
import hangman_words
import hangman_art 

print(hangman_art.logo)
clear = lambda: os.system('cls')

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Create blanks
display = []
guessed_letter = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("\nGuess a letter: ").lower()
    
    clear()
    if guess in guessed_letter:
      print(f"You have already guessed {guess}. Try another.")
      print(f"{' '.join(display)}")   
    else:
      guessed_letter.append(guess)
      letter_present = False
      #Check guessed letteg
      for position in range(word_length):
          letter = chosen_word[position]
          if letter == guess:
              display[position] = letter
              letter_present = True

      if letter_present == True:
        print(f"\n{guess} is present in the word.")

      #Check if user is wrong.
      if guess not in chosen_word:
          print(f"\n{guess} is not presnt in the word. You lose a life.")
          print(hangman_art.stages[lives])
          if lives == 0:
              end_of_game = True
              print("You lose.")
          lives -= 1

      #Join all the elements in the list and turn it into a String.
      print(f"{' '.join(display)}")

      #Check if user has got all letters.
      if "_" not in display:
          end_of_game = True
          print("\nYou win.")