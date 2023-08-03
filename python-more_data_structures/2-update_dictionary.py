#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

    for key, value in a_dictionary():
       
       if key in a_dictionary:
          new_dict = update_dictionary.create(value)
          print(new_dict)
       elif key not in a_dictionary:
          new_dict = update_dictionary.create(key, value)
          print(new_dict)
