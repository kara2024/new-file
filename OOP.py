# Creating class Person
class Person:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender
# Creating the introduce method        
    def introduce(self):
         print(f"Hello, my name is {self.name}. I am {self.age} years old and identify as {self.gender}.")

# Creating an instance of the Person class
person1 = Person("Kara", 18, "Female")
# Calling the introduce method to display the person's information
person1.introduce()