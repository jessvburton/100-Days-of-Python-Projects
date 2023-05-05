from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []
game = True

def deal_card():
  """
  function that uses the cards list to return a random card
  """
  card_delt = random.choice(cards)
  return card_delt

def calculate_score(deck):
  card_total = sum(deck)

  if card_total > 21 and 11 in deck:
    deck.remove(11)
    deck.append(1)
    return
  elif card_total == 21 and len(deck) == 2:
    return 0
  else:
    return card_total

def compare(user, computer):
  user_score = calculate_score(user)
  computer_score = calculate_score(computer)

  if user_score == computer_score:
    print("It's a draw")
  elif computer_score == 0 or user_score > 21:
    print("You lose")
  elif user_score == 0 or computer_score > 21:
    print("You win")
  elif user_score > computer_score:
    print("You win")
  else:
    print("You lose")

def blackjack():
  print(logo)
  
  #Deal the user and computer 2 cards each using deal_card()
  for x in range(2):
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
    
  print(f"Computers first card: {computer_cards[0]}")
  print(f"Your cards are:{user_cards}, current score: {calculate_score(user_cards)}")
  
  if calculate_score(computer_cards) == 0 or calculate_score(user_cards) == 0:
    print("Blackjack!")
  elif calculate_score(computer_cards) >21 or calculate_score(user_cards) >21:
    print("Game over.")
  
  draw_again = True
  
  while draw_again == True:
    play_on = input("Would you like to draw another card? Type 'y' or 'n'\n").lower()
  
    if play_on == 'n':
      draw_again = False
    else:
      user_cards.append(deal_card())
      print(f"Your cards are:{user_cards}, current score: {calculate_score(user_cards)}")
  
  
  if calculate_score(computer_cards) < 17:
    computer_cards.append(deal_card())
  
  compare(user_cards, computer_cards)
  play_again = input("Play again? Type 'y' or 'n'\n").lower()
  if play_again == 'y':
    user_cards.clear()
    computer_cards.clear()
    blackjack()

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n'\n").lower()
if play == 'y':
  blackjack()
