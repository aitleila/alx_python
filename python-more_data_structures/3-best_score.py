#!/usr/bin/python3
def best_score(a_dictionary):

    for key in a_dictionary:

        if key in a_dictionary:
          best_score= max(a_dictionary, key=a_dictionary.get)
          return best_score
        
        elif best_score not in a_dictionary:
           return None
        