value = int(18)
print(type(value))
print(value)

#DAY-8 of 100 days code challange.
#problems on the Modulus operator

#given a two digit number

#Print "Lucky number"

#condition 1 
# The number is a multiple at 9
# One of the digit is 9

number = int(18)
divisible_num = (number % 9)
print(divisible_num)
greather_value = divisible_num

if greather_value:
        print("Lucky number")
else:
        print("Unlucky number")