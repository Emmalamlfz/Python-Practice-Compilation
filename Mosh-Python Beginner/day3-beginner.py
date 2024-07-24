# List
names=['John','Bob','Mosh','Sarah','Mary']
print(names)
for name in names:
    print(name)

print(names[0])
print(names[0:2])

## for loop solution
# Define the list
numbers = [3, 5, 6, 7, 2, 7, 8, 3]

# Initialize the maximum value with the first element
max_value = numbers[0]

# Iterate through the list to find the largest number
for num in numbers:
    if num > max_value:
        max_value = num

# Print the largest number
print(max_value)

# 2D list
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][2])

for row in matrix:
    for item in row:
        print(item)

numbers=[5,2,1,7,5,4]
numbers.append(20)
print(numbers)

numbers.insert(0,77)
print(numbers)

# return the index of the first occurence of the item
print(numbers.index(7))

# check existence
print(50 in numbers)

# count occurence
print(numbers.count(5))
numbers.reverse()
numbers2=numbers.copy()

# write a program to remove the duplicates in a list
numbers=[2,2,4,6,7,8,6,1,3,4]
uniques=[]
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

## tuples: immutable
numbers=(1,2,3,4)
numbers.count(2)
print(numbers[0])

## Unpacking
coordinates=(1,2,3)
x= coordinates[0]
y= coordinates[1]
z= coordinates[2]

## Dictionary
customer={
    "name":"John Smith",
    "age":30,
    "is_verified":True
}
print(customer["name"])
customer["name"]="Jack Smith"

phone=input("Phone:")
digits_mapping={
    "1":"One",
    "2":"Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in phone:
    output+=digits_mapping.get(ch,"!")
print(output)

# mapping words to emoji
message=input(">")
words=message.split(' ')
emojis={
    ":)":"😃",
    ":(":"☹️"
}
output=""
for word in words:
    output+=emojis.get(word,word)
print(output)
