class Animal:
    def __init__(self):
        self.num_eyes=2
    def breathe(self):
        print("inhale,exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__() # inherit from Animal class
    def breathe(self):
        print(self.num_eyes)
        super().breathe() # call parent class's breathe method
        print("doing this underwater")
    def swim(self):
        print("moving in the water")

nemo = Fish()
nemo.breathe()

lists=[1, 2, 3, 4, 5]
tuples=(1,2,3,4,5)
print(lists[1:2]) #[2]
print(lists[1::]) # [2, 3, 4, 5]
print(lists[1::2]) # [2, 4] skip 2
print(lists[::-1]) # [5, 4, 3, 2, 1] reverse a list
print(tuples[::2]) # (1, 3, 5)