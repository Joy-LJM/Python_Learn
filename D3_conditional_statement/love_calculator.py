# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combine_name = (name1 + name2).lower()

count_true = 0
count_true += combine_name.count("t")
count_true += combine_name.count("r")
count_true += combine_name.count("u")
count_true += combine_name.count("e")
count_love = 0
count_love += combine_name.count("l")
count_love += combine_name.count("o")
count_love += combine_name.count("v")
count_love += combine_name.count("e")

love_score = int(f"{count_true}{count_love}")
if (love_score < 10 or love_score > 90):
  print(f"your score is {love_score}, you go together like cock and mentos.")
elif (love_score >= 40 and love_score <= 50):
  print(f"your score is {love_score}, you are alright together.")
else:
  print(f"your score is {love_score}")