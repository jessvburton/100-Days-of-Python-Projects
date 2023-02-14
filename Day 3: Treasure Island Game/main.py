print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

crossroad = input("You're at a crossroad in the forrest. Would you like to go 'left' or 'right'?\n").lower()

if crossroad == "left":
  print("Well done, you've made it further into the forrest.")
  
  river = input("You see a river and are feeling thirsty, do you a.'stop' and take a drink or b.'keep moving'?\n").lower()
  if river == "b" or river == "keep moving":
    print("Good choice.")

    door = input("You are now deep into the forrest and see 3 doors. Which will you choose? 'Red', 'Blue', 'Yellow' or 'Keep moving'?\n").lower()
    if door == "yellow":
      print("You found the treasure. You win!")
    elif door == "blue":
      print("You get burned by fire. GAME OVER!")
    elif door == "red":
      print("You fall into a HUGE hole, breaking both legs. GAME OVER!")
    else:
        print("GAME OVER!")
  else: 
    print("Oh no, you didn't see the crocodial waiting beneath the surface. GAME OVER!")
else:
  print("You get eaten by a lion. GAME OVER!")
