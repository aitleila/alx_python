#!/usr/bin/python3

import random
number = random.randint(-10000, 10000)

Last_digit = abs(number) % 10

print ("Last digit of {}" " is {}". format(number,Last_digit),end="")

if number > 0:
    
    if Last_digit > 5:
        print(" and is greater than 5 ")
    elif Last_digit == 0:
        print(" and is 0 ")
    else:
        print(" and is less than 6 and not 0 ")

elif number <= 0:
Last_digit = -Last_digit

   
    if Last_digit == 0:
        print(" and is 0 ")
    else:
        print(" and is less than 6 and not 0 ")



   



