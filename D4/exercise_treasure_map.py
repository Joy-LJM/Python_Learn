# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
row_list = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") #column 2, row 3 would be entered as:23
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column=int(position[0])-1
row=int(position[1])-1
print(column,row)
row_list[row][column]= "x"










#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")