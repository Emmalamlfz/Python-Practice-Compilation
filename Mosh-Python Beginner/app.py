print('Hello world!')

# Variable
age = 20
age = 30
print(age)

# Exercise: Check in a patient named John Smith; he's 20 years old; he's a new patient
name="John Smith"
age=20

# Receive input
name=input("What is your name?")
print("Hello"+name)

# Type Conversion
birth_year=input("Enter your birth year: ")
age=2020-int(birth_year)
print(age)
int()
float()
bool()
str()

first=input("First: ")
second=input("Second: ")
sum=int(first)+int(second)
print(sum)

# String - 这些功能是specifically belongs to String type variables,被叫做method
course="Python for Beginners"
print(course.upper())
print(course.find('y'))
print(course)

# Arithmetic Operator:+-*% / //
# Logical Operator: Or, and, not
price=5
print(price>10 or price<30)

# If Statement
temperature=35

if temperature >30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature>20:
    print("It's a nice day")
print("Done")

## exercise
weight=int(input("Weight: "))
unit=input("(K)g or (L)bs: ")
if unit.upper()=="K":
    converted=weight/0.45
    print("Weight in Lbs: "+ str(converted))
else:
    converted=weight*0.45
    print("Weight in Kgs:"+ str(converted))

# While loops

i=1
while i <=5:
    print(i)
    i=i+1


while i <= 5:
    print(i*"*")
    i=i+1

# Lists
names=["John","Sam","Susan"]
print(names[0])
print(names[-1])

numbers=[1,2,3,4,5]
numbers.append(3)
numbers.insert(1,-1)
print(numbers)

# For loops
numbers=[1,2,3,4,5]
for item in numbers:
    print(item)

i=0
while i<len(numbers):
    print(numbers[i])
    i+i+1

# The range() function
numbers=range(5)
for number in numbers:
    print(number)

# Tuples - immutable/unchangeable
numbers=(1,2,3)
numbers.count()
