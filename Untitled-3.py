#indexing Concepts with slicing 
name = "This is kalyan"
print(name[2:7])
 
name = "rammam"
print(name[1:])

# Data Type Conversion
a= False
print(type(a))

#Data Type Conversion
a=10.2
a= int(a)
print(type(a))
print(a)


# Creating a list
numbers = [1, 2, 3, 4, 5]

# Indexing and slicing
print(numbers[1:3])

# Appending an item to the list
numbers.append(6)
print(numbers)

# Removing an item from the list
numbers.remove(3)
print(numbers)

# Exception handling
try:
    # Accessing an index that doesn't exist
    print(numbers[10])
except IndexError:
    print("Index out of range")

