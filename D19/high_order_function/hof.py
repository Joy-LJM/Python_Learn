def calculate(n1,n2,func):
    return func(n1,n2)
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
result=calculate(3,4,add) # calculate is a hof, taking a function as input
print(result)