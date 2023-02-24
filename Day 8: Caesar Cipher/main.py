alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alpha = ['A', 'B', 'C', 'D', 'E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
plain_text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift):
  cipher_text = ""
  for l in plain_text:
    if l.islower():
      l_position = alphabet.index(l)
      new_position = (l_position + shift) % 26
      cipher_text += alphabet[new_position]
    elif l.upper():
      l_position = alpha.index(l)
      new_position = (l_position + shift) % 26
      cipher_text += alpha[new_position]
  print(f"The encoded text is {cipher_text}")

encrypt(plain_text = plain_text, shift = shift)
