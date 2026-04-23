'''
Use class-level attribution(root of the class) only for values that are the same for every object.

Example:
-Number of weels on a car
-Pi constant
-Configuration shared by all instances
-Version number...
'''
class Car:
    weels = 4 # same for all cars as a default.

'''
These attributes live on the class, not the object

Use constructor (_init_) for the instance-specific data. They are unique per object.

Examples:
- Car colour
- Max speed
- current car
- registration number
'''
class car:
    weels = 4 # Shared by defults by all cars

    def __init__(self, color, max_speed):
        self.color = color
        self.max_speed = max_speed
        self.current_speed = 0

'''
Every time you create a new object, constructor (_init_) runs and gives that specific object its own attributes.

Why not put obeject-specific attributes in the root ? Because attribute in the root are shared unless overwritten.

For example:
'''

class Person:
    def __init__(self):
        self.hobbies = []

p1 = Person()
p2 = Person()

p1.hobbies.append('Football')
p1.hobbies.append('Reading')
p2.hobbies.append('Making music')

print(p2.hobbies) # OOPS; they share the same list !! That is not what i want:'

'''
If the list was inside _init_, each would get its own list.
'''
class Student:
    def __init__(self):
        self.hobbies = [] # unique list for each object

s1 = Student()
s2 = Student()

s1.hobbies.append('cricket')
s2.hobbies.append('chess')
print(s2.hobbies) # ['chess'] - works as expected