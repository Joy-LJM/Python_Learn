def add(*args):#many positional arguments; args is a tuple (1,2,3); asterix * is indispensable
    total=0
    for num in args:
        total+=num
    return total
result=add(1,2,3)
print(result)

def calculate(n,**kwargs): # many keyword arguments; kwargs is a dictionary
    print(kwargs)
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    print(n)
print(calculate(2,add=3,multiply=5))

# dic={'add': 3, 'multiply': 5}
# print(dic.items())
# print(dic.keys())
# print(dic.values())

class Car:
    def __init__(self,**kwargs):
        self.speed=100
        self.brand=kwargs["brand"] #if not passing parameter brand, there will be an error
        # self.brand=kwargs.get("brand") #if not passing parameter brand, there will be none
        self.model=kwargs.get("model")
        self.color=kwargs.get("color")
car=Car(brand="Nissan",model="GTR")
print(car.model)