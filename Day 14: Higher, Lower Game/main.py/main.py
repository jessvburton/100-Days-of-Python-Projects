import art
from game_data import data
from random import randint
from replit import clear
from functions import *

score = 0
play = True
person_a = []
person_b = []

print(art.logo)
a_person, a_name, a_followers, a_description, a_country = get_person_details()
b_person, b_name, b_followers, b_description, b_country = get_person_details()

if person_a == person_b:
  b_person, b_name, b_followers, b_description, b_country = get_person_details()

while play == True:
  print(f"Compare A: {a_name}, {a_description}, from {a_country}")
  print(art.vs)
  print(f"Compare B: {b_name}, {b_description}, from {b_country}")

  answer = input("Who has more followers? A or B?\n").upper()

  most_followers = compare(a_followers, b_followers)

  if answer == most_followers:
    score += 1
    clear()
    print(art.logo)
    print(f"You're right, current score:{score}")
  else:
    print(
      f"That's incorrect. '{most_followers}' was the correct answer. Your score is {score}"
    )
    play = False

  if b_followers > a_followers:
    a_name = b_name
    a_followers = b_followers
    a_description = b_description
    a_country = b_country

    if person_a == person_b:
      b_person, b_name, b_followers, b_description, b_country = get_person_details()
  else:
    b_person, b_name, b_followers, b_description, b_country = get_person_details()
