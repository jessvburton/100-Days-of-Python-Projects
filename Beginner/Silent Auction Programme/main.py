from replit import clear
import art

# Show logo
print(art.logo)

# Variables
auction = {}
auction_live = True
highest_bid = 0
winner = ""

# Function to take name and bid as input and put into a dictionary
def bidder(name,bid):
  name = input("What is your name?\n")
  bid = int(input("How much would you like to bid?\n"))
  auction.update({name:bid})
  print(auction)

# Call function
bidder("name","bid")

# While statement
while auction_live == True:
  play_on = input("Are there any other bidders?\n").lower()
  if play_on == "yes":
    clear()
    bidder("name","bid")
  elif play_on == "no":
    for key in auction:
      bid = auction[key]
      if bid > highest_bid:
        highest_bid = bid
        winner = key        
    print(f"The winner is {winner}!")
    auction_live = False
  else:
      print("Incorrect input")
