#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    for i in matrix:
        new_matrix = (pow(i*2), matrix)
    return new_matrix