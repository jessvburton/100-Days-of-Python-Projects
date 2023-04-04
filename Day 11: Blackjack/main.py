from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer = []
player1 = []

def deal(): # for when player wants to draw another card
  player1.append(random.choice(cards)) #deal random card from cards
  computer.append(random.choice(cards)) #append to computer and player1 lists
  player1_score = sum(player1)
  print(f"Your cards:{player1}, current score: {player1_score}") #print cards player1 has & provide total for player1
  print(f"Computers first card: {computer[0]}") #print computers first card
  
def blackjack():
  more = True
  print(logo)

  player1.append(random.choice(cards))
  computer.append(random.choice(cards))
  deal()

  # if 21 on first hand set to 0 and exit game

  while more == True:
    another = input("Take another card? Type 'y' or 'n'\n")
    if another == 'y':
      deal()
    else:
      # change 11 to 1 if total more than 21
      
      player1_score = sum(player1)
      computer_score = sum(computer)

      print(f"Your final hand:{player1}, final score: {player1_score}") #player1 cards and total
      print(f"Computers final hand:{computer}, final score: {computer_score}") #computer cards and total

      if player1_score <= 21 and computer_score <= 21: # checks both are equal to or less than 21
        if player1_score > computer_score:
          print("You win.")
        elif player1_score == computer_score:
          print("It's a draw.")
        else:
          print("You lose.")
      elif player1_score > 21 and computer_score > 21:
        print("You both lose.")
      elif player1_score > 21 or computer_score > 21:
        if player1_score > 21:
          print("You lose.")
        else:
          print("You win.")

      re_play = input("Do you want to play another game of Blackjack? Type 'y' or 'n'\n").lower()
      if re_play == 'y':
        player1.clear()
        computer.clear()
        more = False
        blackjack()
      else:
        more = False
      
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()
if play == 'y':
  blackjack()
