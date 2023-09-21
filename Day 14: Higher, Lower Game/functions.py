from random import randint

def compare(a_followers, b_followers):
  if a_followers > b_followers:
    most_followers = 'A'
  elif b_followers > a_followers:
    most_followers = 'B'
  return most_followers

def get_person_details():
  person = randint(0, 49)
  name = data[person].get('name')
  followers = data[person].get('follower_count')
  description = data[person].get('description')
  country = data[person].get('country')
  return person, name, followers, description, country
