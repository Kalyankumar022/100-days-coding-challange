#problem Solving &Debugging Questions.
#write a Program to check if the given two digit num is > 25 is first digit 
# num is greather than its second digit number
#Condition Applied

#Reading input
#two digit num is greather than 25 

number = "25"
first_num = int(number[0])
print(first_num)

word_len = len(number)
print(word_len)

last_name =int(number[1])

is_my_numberisgreather = (first_num>last_name)and (first_num<last_name)

print(is_my_numberisgreather)

if is_my_numberisgreather:
        print("possible")
else:
        print("not possible")
        
        
# problem soving and debugging 
#modulus operator(%)

print(3%2)
print(9%4) 
print(8%2)
print(121%17)

#write a program that determines. if the given number is "(Even or odd)" using modulus operator

number = int(9)
value = (number% 2)
print(value)
is_value = value == 0

if is_value:
        print("even")
else:
        print("odd")


def is_greater_than_25(number):
    if number > 25:
        return True
    else:
        return False
#


def check_digit_order(number):
    first_num = int(number[0])
    last_num = int(number[1])
    if first_num > last_num:
        return True
    else:
        return False

def is_possible(number):
    if is_greater_than_25(number) and check_digit_order(number):
        return True
    else:
        return False

number = "25"
if is_possible(number):
    print("Possible")
else:
    print("Not Possible")


a = int(1)
b = int(2)

a = b*3
print(a)

number = a<=10
print(number)