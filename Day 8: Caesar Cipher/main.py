from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
play = True

def caesar(direction, text, shift):
  output_text = ""
  if direction == "decode":
    shift *= -1
  for l in text:
    #TODO: What happens if the user enters a number/symbol/space?
    if l.islower():
      l_position = alphabet.index(l)
      new_position = (l_position + shift) % 26
      output_text += alphabet[new_position]
    elif l.upper():
      l_position = alpha.index(l)
      new_position = (l_position + shift) % 26
      output_text += alpha[new_position]
    elif l.isspace():
      output_text 
  print(f"The {direction}d text is {output_text}")

print(logo)

while play == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))
  
  caesar(direction = direction, text = text, shift = shift)

  retry = input("Would you like to go again? 'Y' or 'N'\n")

  if retry == "N":
    play = False
