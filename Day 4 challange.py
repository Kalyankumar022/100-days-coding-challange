

#IF Conditional statements

c = 20
d = 40

if d>c:
        print("positive")
print("End")


        
#writing a code 

if True:
        print("positive")
        print("Not positive")

a = "Hello"
print(a + " " + "Kalyan")

#if conditional statements

kalyan = int(8)
print(type(kalyan))

if kalyan>0:
            print("Not ok")
else:
            print("condition not satisfied")
            
# Another Example forn if Concepts

a  = int(40)
b = int(30)            
c = a<b and b<a

if True:
            print("Code is Working")
else:
            print("Condition not satisfied")

#if Condition Statement

age = int(24)
print(type(age))
Y= "years old"
Z = "now"
print("Kalyan has " + str(age) + Y+" "+ Z)

# Get the current year
current_year = 2022

# Ask the user for their birth year
birth_year = int(input("Enter your birth year: "))

# Check if the birth year is a leap year
if birth_year % 4 == 0:
    if birth_year % 100 == 0:
        if birth_year % 400 == 0:
            print(f"{birth_year} is a leap year.")
        else:
            print(f"{birth_year} is not a leap year.")
    else:
        print(f"{birth_year} is a leap year.")
else:
    print(f"{birth_year} is not a leap year.")

# Check if the person is currently a teenager
if birth_year + 13 > current_year:
    print("You are a teenager.")
elif birth_year + 13 == current_year:
    print("You will be a teenager this year.")
else:
    print("You are not a teenager.")

#Problem Solving using relational methods

