#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
    square_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num**2)
            square_matrix.append(num**2)
            square_matrix = square_matrix_simple(matrix)

    return square_matrix

