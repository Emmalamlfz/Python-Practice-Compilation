x=-2.9
print(abs(x))

import math
print(math.ceil(x))

# If statement
is_hot=True

if is_hot:
    print("It's a hot day")
else:
    print("It's a cold day")
    print("Wear warm clothes")
print("Enjoy your day")

# logical operator : when we have multiple conditions
has_high_income=True
has_good_credit=True

if has_high_income and has_good_credit:
    print("Eligible for loan")

has_criminal_record=True
if has_good_credit and not has_criminal_record:
    print("Eligible")

# comparison operator ><=
temp=35
if temp>35:
    print("it's very hot")
elif temp>20:
    print("mild weather")
else:
    print("It's cold")

# While loops
a=1
while a<=5:
    print(a)
    a+=1

# Guessing game
secret_num=9
guess_count=0 # i represent the number of guesses
guess_limit=3
while guess_count<guess_limit:
    guess=input("Guess: ")
    guess_count+=1
    if guess==secret_num:
        print("You won!")
        break
    else:
        print("False")

# Building a car game
command=""
while command.lower()!="quit":
    command=input(">")
    if command.lower() == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command.lower() == "start":
        print("to start the car")
    elif command.lower() == "stop":
        print("to stop the car")
    else:
        print("quit")
        break

# range function
for item in range(10):
    print(item)  # 10 is not included

# Nested loop
for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

# find the largest number in the list
numbers=[3,4,6,7,8,3,1]
max=numbers[0]
for number in numbers:
    if number>max:
        max=number
print(max)
