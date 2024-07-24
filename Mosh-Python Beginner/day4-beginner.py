# Classes 类定义
# Class name 首字母需要大写
#class Point:
#    def move(self):
#        print("move")
#    def draw(self):


# with this class we create new object


# Constructors
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

point=Point(10,20)
print(point.x)

# Define a class called "Person", should have "name" attribute, and talk()
class Person:
    def talk(self):
        print("talk")

john=Person()
john.talk()

import converter
from converter import kg_to_lbs
print(converter.kg_to_lbs(70))

kg_to_lbs(55)

# build a module that find the max number in the list
from max import find_max
list1=[2,4,6,2,3,4,8,5]

