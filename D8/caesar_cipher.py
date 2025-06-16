alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
#Don't change the code above 👆

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# hello 2
# def encrypt(text,shift):
#   encrypt_text="" # j
#   for letter in text:
#     idx=alphabet.index(letter)
#     shifted_position=idx+shift #7->9
#     #make sure it won't out of range
#     shifted_position%=len(alphabet) #3%52=3 56%52=4
#     encrypt_text+=alphabet[shifted_position]
#   print(f"Here is the encrypted result: {encrypt_text}")
# encrypt(text,shift)

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# def decrypt(text,shift):
#   decrypt_text="" 
#   for letter in text:
#     idx=alphabet.index(letter)
#     shifted_position=idx-shift 
#     #make sure it won't out of range
#     shifted_position%=len(alphabet) #3%52=3 56%52=4
#     decrypt_text+=alphabet[shifted_position]
#   print(f"Here is the decrypted result: {decrypt_text}")
# decrypt(text,shift)

# combine 2 functions
def caesar(type,text,shift_amount):
      output_text="" 
      if type=="decode": # should be outside the loop,or it will be positive
        shift_amount*=-1
      for letter in text:
        idx=alphabet.index(letter)
        shifted_position=idx+shift_amount #3+5*-1 === 3-5
        shifted_position%=len(alphabet) 
        output_text+=alphabet[shifted_position]
      print(f"Here is the  result: {output_text}")

caesar(direction,text,shift)