#Nested Conditional statements

condition_a = True
condition_b = False

if condition_a:
        print("block1")
        if condition_b:
                print("block2")
        else:
                print("block3")
            
print("block4")

#question

#write a program to print the greates among the three numbers

a = int(2)
b  = int(3)
c   = int(4)

is_a_greather = (a>b) and (a>c)

is_b_greather = (b>a) and (b>c)

is_c_greather = (c>a) and (c>b)

if is_a_greather:
            print(a)
else:
            is_c_greather
            if is_c_greather:
                        print(c)
            else:
                        if is_b_greather:
                                    print(b)
                        else:
                                    print("All are equal")

#Another Question:

x = int(3)
y = int(2)
z = int(4)

is_x_greather = (x>y) and (x>z)

print(is_x_greather)

if is_x_greather:
            print("x")
else:
        is_y_greather = (y>x) and (y>z)
        if is_y_greather:
                    print(y)
        else:
                is_z_greather = (z>x) and (z>y)
                if is_z_greather:
                            print(z)
                            
#elif condition'

condition_a = False
condition_b = True
condition_c = True

if condition_a:
            print("passes number")
elif condition_b:
            print("Number not passed")
else:
            print("else num passed")
            