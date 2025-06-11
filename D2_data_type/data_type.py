height = input("Input your height in m: ")
weight = input("Input your weight in kg: ")
bmi = int(weight) / (float(height)**2)
print(int(bmi)) # remove decimal


print("string"[-1]) #print the last character of the string: g
print("string"[0:3]) #print the first 3 characters of the string: str
print("string"[0:]) #print the whole string: string
print("string"[:3]) #print the first 3 characters of the string:str
print("string"[0:3:2]) #print the first 3 characters of the string with a step of 2: sr
print("string"[::-1]) #print the string in reverse: gnirts
print("string"[::-2]) #print the string in reverse with a step of 2: git
print("string"[::-3]) #print the string in reverse with a step of 3: gr

print(round(8/3))#2.6666666666666665->3
print(round(8/3,2))#2.6666666666666665->2.67
print(8//3)#2 #integer/floor division
print(type(8/3))#float
print(type(8//3))#int

#f string example 
score=0
isWinning=False
print(f"my score is {score}, you are winning is {isWinning}")

# practice: Your life in weeks
age = input("What is your current age? ")
age_as_int = int(age)
max_age = 90
remain_year = max_age - age_as_int
days_left = remain_year * 365
weeks_left = remain_year * 52
months_left = remain_year * 12
print(
    f"You have {days_left} days,{weeks_left} weeks, and {months_left} months left."
)
