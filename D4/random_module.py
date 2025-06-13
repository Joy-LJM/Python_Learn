import random
import pi_module

# print(random.randint(1,9))
# print(pi_module.pi)

#random float between 0 and 1
random_float=random.random()
print(random_float)

#random number between 0 and 5
print(random.random()*5)

random_int=random.randint(0,1)# include 1
print(random_int)
if(random_int==0):
    print("Heads")
else:
    print("Tails")