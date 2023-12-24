first_line = int(-1)
second_line = int(1)
result_line = first_line<second_line
print(result_line)

if result_line:
        print(second_line)

else:
        print(first_line)

#Writing another code 

first_number = 5
first_number = int(5)
print(type(first_number))
second_number = 9 
result =first_number>second_number
print(result)

if result:
            print(second_number)
else:
            print(first_number)
            


#Another programming questions

#for example if the given input word is "qwenty@2023" the output should be "q*******3"

#note observe the number ofcharacters b/w two Ends is equal to the number of asterists characters(*) in the input

#writing programme
#out put will be = "q*********3"
name = "qwenty@2023"
first_letter = name[0]

# To Define word length
word_len = len(name)
print(word_len)
last_number = name[word_len-1]
num_stars = "*" *(word_len-2) 
print(first_letter + num_stars + last_number)

#writing another Programm

#output  = password@2023

name1 = "password@2023"
first_let = name1[0]
word_length = len(name1)
print(word_length)
last_nm = name1[word_length-2]
stars = "*"* (word_length-1)
print(first_let+stars+last_nm)


num = int(52)
print(type(num))

if num>0:
            print("True")
else:
            print("False")
  