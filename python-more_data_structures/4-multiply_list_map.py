 #!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = [x * number for x in my_list if x % number == 0]