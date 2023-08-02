#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square_matrix = []
    for row in matrix:
        for i, num in matrix(row):
            new_row = []
            for num in row:
               new_row.append(num**2)
               square_matrix.append(num**2)
    return square_matrix
