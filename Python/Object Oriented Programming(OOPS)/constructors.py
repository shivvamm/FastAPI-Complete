"""
Constructros are used to instantiate the object
with or without starting values 
"""


from Arena_Project.Enemy import Enemy

enemy = Enemy()
# the calling of object is the calling of consturctors

# Types of constructors 

# 1. Default / Empty consturctor


class man:
    name:str
    age: int
    weight:int

# Here self refers to the current class/object
# Below is the contructor if we dont create it will automatically be created
    def __init__(self):
        pass

    def talk(self):
        print(f"Hello my name is {self.name}")

jhon = man()

jhon.name = 'jhon'


# 2. No argument Constructor 
# similar to he default one but here insted of pass we 
# write some functionality 

class animal:
    name:str
    paws: int

# Here self refers to the current class/object
# Below is the contructor if we dont create it will automatically be created
# It basically means to do something when the object is instantiate
    def __init__(self):
        print("New animal is in the zoo")

    def talk(self):
        print(f"Hello the animal is {self.name}")


lion = animal()
lion.name = 'lion'

# 3. Parameter Constructor
# here we will be passing parameters while creating the obejct 

class Enemy:
    def __init__(self,type,health=10,attack=1):
        self.type = type
        self.health = health
        self.attack = attack
    
    def talk(self):
        print("I am an enemy")

enemy = Enemy("Orge")
print(enemy.health)
enemy.talk()
