#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):

   for key in a_dictionary:
      if key in a_dictionary:
         a_dictionary.update({"language": "Python"})    
      elif key not in a_dictionary:
         a_dictionary.update({'city' : "San Francisco"})    
         


