#Step 4

import random
import requests

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
# word_list = ["ardvark", "baboon", "camel"]
api_url = "https://random-word-api.herokuapp.com/word"
response = requests.get(api_url)
chosen_word = response.json()[0]
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

lives = 6

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')
guessed_letters = []

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    if len(guessed_letters)!=0:
      print("Guessed Letters: ",",".join(guessed_letters))
    
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
            


    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in chosen_word:
      guessed_letters.append(guess)
      lives -= 1
      if lives == 0:
       end_of_game = True
       print("The word was: ", chosen_word) 
       print("You lose.") 

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.

    # if lives == 6:
    #   print(stages[-1])
    # elif lives == 5:
    #   print (stages[-2])
    # elif lives == 4:
    #   print (stages[-3])
    # elif lives == 3:
    #   print (stages[-4])
    # elif lives == 2:
    #   print (stages[-5])
    # elif lives == 1:
    #   print (stages[-6])
    # else:
    #   print (stages[-7])

    print(stages[lives])