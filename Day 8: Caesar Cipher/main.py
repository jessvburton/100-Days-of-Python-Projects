from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
play = True

def caesar(direction, text, shift):
  output_text = ""
  if direction == "decode":
    shift *= -1
  for char in text:
    if char in alphabet:
      l_position = alphabet.index(char)
      new_position = (l_position + shift) % 26
      output_text += alphabet[new_position]
    elif char in alpha:
      l_position = alpha.index(char)
      new_position = (l_position + shift) % 26
      output_text += alpha[new_position]
    else:
      output_text += char
  print(f"The {direction}d text is {output_text}")

print(logo)

while play == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n")
  shift = int(input("Type the shift number:\n"))
  
  caesar(direction = direction, text = text, shift = shift)

  retry = input("Would you like to go again? 'Y' or 'N'\n").upper()

  if retry == "N":
    play = False
