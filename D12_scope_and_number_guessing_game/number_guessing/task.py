import art
import random
print(art.logo)

def guess_num(attempts):
  random_num=random.randint(1,100)
  # print(random_num)
  count=attempts
  while count>0:
      print(f"You have {count} attempts to guess the number.")
      guess=int(input("Make a guess: "))
      if(count!=1):
        count-=1
        if guess>random_num:
          print("Too high.\nGuess again.")
        elif guess< random_num:
          print("Too low.\nGuess again.")
        else:
          print(f"You got it. The answer was {random_num}")
          count=0
      elif count ==1 and guess !=random_num:
        print("You've run out of guesses. Refresh the page to run again.")
        count=0

print("Welcome to the Number Guessing Game!")
print("I am think of a number between 1 and 100.")
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
if difficulty == 'easy':
  attempts=EASY_LEVEL_TURNS
  guess_num(attempts)
else:
  attempts=HARD_LEVEL_TURNS
  guess_num(attempts)


