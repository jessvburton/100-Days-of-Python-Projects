import random
import art

# Intro
print("Welcome to a game of rock, paper, scissors")

# Users input
player1 = input("What do you choose? 'Rock', 'Paper', or 'Scissors'\n").lower()
print(f"You chose {player1}!\n")
if player1 == "rock":
  print(art.r)
elif player1 == "paper":
  print(art.p)
elif player1 == "scissors":
  print(art.s)
else:
  print("Invalid input, try again.")

# Computer response
options = ["rock", "paper", "scissors"]
cp = random.choice(options)
print(f"Computer chose {cp}!")

if cp == "rock":
  print(art.r)
elif cp == "paper":
  print(art.p)
elif cp == "scissors":
  print(art.s)

# Draw results
if player1 == cp:
  print("It's a draw...")

# Rock wins
if player1 == "rock" and cp == "scissors":
  print("You win!")
if player1 == "scissors" and cp == "rock":
  print("You lose!")

# Paper wins
if player1 == "paper" and cp == "rock":
  print("You win!")
if player1 == "rock" and cp == "paper":
  print("You lose!")

# Scissors win
if player1 == "scissors" and cp == "paper":
  print("You win!")
if player1 == "paper" and cp == "scissors":
  print("You lose!")
