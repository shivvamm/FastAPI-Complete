# Self is used to refer to the current object and 
#super is used to refer to the parent class

# Self i used when there is a need to differenciate 
# betweenn variable and parameters


#Super is used to call the parent class methods 
# or constructors 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

# iinherits form the Person class
class Student(Person):
    def __init__(self, name, age, rollno):
        #Calling the person 
        super().__init__(name=name,age=age)
        # Here it is refering to the degree property which is different from the degree parameter
        self.rollno = rollno


