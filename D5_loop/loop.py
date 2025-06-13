# total=0
# for item in range(1,101): # not inclusive of last
#   total+=item
# print(total)

for number in range(1,101):
    if(number%3==0 and number%5==0):
        print("FizzBuzz")
    elif(number%3==0):
        print("Fizz")
    elif(number%5==0):
        print("Buzz")
    else:
        print(number)