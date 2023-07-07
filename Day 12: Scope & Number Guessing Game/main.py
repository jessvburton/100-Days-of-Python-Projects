import art as a
import random as r

random_number = r.randint(1,100)
guess = 0
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
  difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if difficulty_level == 'easy':
    return EASY_LEVEL_TURNS
  elif difficulty_level == 'hard':
    return HARD_LEVEL_TURNS
  else:
    print("Incorrect input.")

def check_answer(guess, random_number, number_of_guesses):
  if guess > random_number:
    print("Too high.")
    return number_of_guesses - 1
  elif guess < random_number:
    print("Too low.")
    return number_of_guesses - 1
  else:
    print(f"You win! The number was {random_number}")

print(a.logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

number_of_guesses = set_difficulty()

while guess != random_number:  
  print(f"You have {number_of_guesses} attempts remaining to guess the number.")
  
  guess = int(input("Make a guess: "))

  number_of_guesses = check_answer(guess, random_number, number_of_guesses)
  if number_of_guesses == 0:
    print(f"Game over! The number was {random_number}")
    guess = random_number
  else:
    print("Guess again.")
