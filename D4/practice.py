import random
# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Get the total number of items in list.
print(names)
random_idx=random.randint(0,len(names)-1)
print(f"{names[random_idx]} is going to buy the meal today")