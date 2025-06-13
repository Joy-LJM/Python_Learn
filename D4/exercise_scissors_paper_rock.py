rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
choose_list=[rock,paper,scissors]
user_choose=int(input("What do you choose? Type 0 for rock, 1 for Paper or 2 for scissors\n"))
if(user_choose>2 or user_choose<0):
  print("You input valid number, you lost")
  
else:
  print(choose_list[user_choose])
  computer_choose=random.randint(0,2)
  print(f"Computer chose:\n{choose_list[computer_choose]}")
  if(user_choose==computer_choose):
    print("Draw")
  elif(user_choose==0 and computer_choose==1 or user_choose==1 and computer_choose==2 or user_choose==2 and computer_choose==0):
    print("You lost")

  else:
    print("You Win")

