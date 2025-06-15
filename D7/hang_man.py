import random
word_list=["aardvark","baboon","camel"]
chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# all_correct=False
i=0
while i<len(chosen_word):
    i+=1
    placeholder+="_"

# space_list=list(placeholder)
# while(not all_correct):
#   print(f"Word to guess:{placeholder}")
#   letter=input("Guess a letter:").lower()
#   idx=word.find(letter)

#   if(idx!=-1):
#     space_list[idx]=letter
#     placeholder="".join(space_list)
#     print("right")
#   else:
#     print("false")

game_over=False
correct_letters=[]
lives=6

while not game_over:
  print(f"******************{lives}/6 lives left******************")
  guess=input("Guess a letter:").lower()
  display=""
  if(guess in correct_letters):
        print(f"You already guess {guess}")
  for letter in chosen_word:
      # check current letter
      if lives==0:
         print(f"It was {chosen_word}. You lose.")
      else:
        if letter ==guess:
          display+=letter
          correct_letters.append(guess)
          # check previous letter
        elif letter in correct_letters:
          display+=letter
        else:
          display+="_"
  print(display)

  if(guess not in chosen_word):
     print(f"The letter: {guess} is not in the word. You lost a lives")
     lives-=1
     if lives==0:
        game_over=True
        print("You lost!")

  if "_" not in display:
     game_over=True
     print("You win!")
  print(stages[lives])