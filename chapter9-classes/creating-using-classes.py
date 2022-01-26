""" write classes that represent real world thins and situations,
create objects based on thses classes

instantiation - making an object from a class, and you work with instances of a class"""

# define class with upper case
class Dog:
# comment describing what the class is
    """simple attmept to model a dog"""
# function that is part of a class is a method
# self parameter is req. in the method defination
    def __init__(self, name, age):
        """initialize name and age attributes"""
        """ any variable prefixed with self is available to every method in the
        class, and able to access these variable thru any instance created"""
        """variables that are accessible thru instances like this are called
        attributes"""
        self.name = name
        self.age = age
        """since the methods here are simple & just prints not complex like future"""
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f'{self.name} is now sitting.')

    def rollover(self):
        """simulate a dog rolling over in response to a command"""
        print(f'{self.name} rolled over.')

# Making an instance from a class
"""think of a class as a set of instructions for how to make an instance, the
class Dog is a set of instructions that tells PY how to make individual
instances representing specific dogs"""

"""create a variable, assign the Dog class with the parameters filled in
this will call the __init__ method with the arguments inside of it..line 18-19
this method creates an instance representing the info provided"""
my_dog = Dog('Rocky',12)
# access the attribute of an instance, use . notation, ex: variable name.parameter
print(f'My first dog is {my_dog.name} and {my_dog.age} years old.')

# Calling Methods
