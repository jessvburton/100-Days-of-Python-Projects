import random
import art as a 
import words as w

# Lists, variables & counters
display = []
chosen_word = random.choice(w.word_list)
word_legth = len(chosen_word)
lives = 6
end_of_game = False

# print logo
print(a.logo)

#For each letter in the chosen_word, add a "_" to 'display'.
for i in chosen_word:
  display += "_"
print(f"{' '.join(display)}")

# While loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_").
while not end_of_game:
  # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
  guess = input("Please guess a letter...\n").lower()

  if guess in display:
    print(f"You have already guessed the letter {guess}")
  # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
  for p in range(word_legth):
    letter = chosen_word[p]
    if letter == guess:
      display[p] = letter
      
  if guess not in chosen_word:
    print(f"{guess} is not in the word, you have lost 1 life.")
    lives -= 1
    print(f"Lives remaining: {lives}")
    print(a.stages[lives]) # ascii art
    if lives == 0:
      end_of_game = True
      print(f"You lose, the word was {chosen_word}")

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")
  
  if "_" not in display:
    end_of_game = True
    print("You win!")
