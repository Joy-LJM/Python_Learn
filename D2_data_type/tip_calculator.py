# Tip Calculator
print("Welcome to the tip calculator.")
bill=float(input("what was the total bill?$"))
tip=int(input("What percentage tip would you like to give?10,12,or 15?"))
people=int(input("How many people to split the bill?"))

include_tip=tip/100*bill+bill
bill_per_person=include_tip/people
# each=round(bill_per_person,2) #33.6
each="{:.2f}".format(bill_per_person)  # format into 2 decimal places: 33.60
print(f"Each person should pay: ${each}")