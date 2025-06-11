height = input("Input your height in m: ")
weight = input("Input your weight in kg: ")

bmi = int(weight) / (float(height)**2)
print(int(bmi)) # remove decimal


print("string"[-1]) #print the last character of the string: g
print("string"[0:3]) #print the first 3 characters of the string: str
print("string"[0:]) #print the whole string: string
print("string"[:3]) #print the first 3 characters of the string:str
print("string"[0:3:2]) #print the first 3 characters of the string with a step of 2: st?
print("string"[::-1]) #print the string in reverse: gnirts
print("string"[::-2]) #print the string in reverse with a step of 2: git
print("string"[::-3]) #print the string in reverse with a step of 3: gn
