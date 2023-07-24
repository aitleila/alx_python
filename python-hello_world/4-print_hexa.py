  # take input from user
n = 97
 
# loop through the numbers from 1 to N
for i in range(0, n+1):
    # use string formatting to convert the number to hexadecimal
    hex_value = "{0:x}".format(i)
    # print the hexadecimal value
    print(hex_value)
