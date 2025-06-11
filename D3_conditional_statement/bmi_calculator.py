height = float(input("enter your height in m:"))
weight = float(input("enter your weight in kg:"))

bmi =round(weight / height**2)
if (bmi < 18.5):
  print(f"your bmi is {bmi}, you're under weight")
elif (bmi<25):# bmi > 18.5 and bmi < 25
  print(f"your bmi is {bmi}, you're normal weight")
elif (bmi < 30): # bmi > 25 and bmi < 30
  print(f"your bmi is {bmi}, you're over weight")
elif (bmi < 35): # bmi > 30 and bmi < 35
  print("obese")
else:
  print("clinically obese")