## function
def greet_user():
    print("Hi there!")
    print("Welcome aboard!")

greet_user()

## Parameter
def greet(name):
    print(f'Hi {name}!')
    print('Welcome!')

print(greet("John"))

## Keyword Arguments
def greet_user(first_name, last_name):
    print(f'Hi { first_name} {last_name}!')
    print('Welcome aboard')
print("Start")
print(greet_user("John","Smith"))
print("Finish")

# Return statement
def square(number):
    return number*number

result=square(3)
print(result)


