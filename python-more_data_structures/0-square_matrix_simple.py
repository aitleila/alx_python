#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    square_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num**2)
        square_matrix.append(num**2)

    return square_matrix

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

output_matrix = square_matrix_simple(input_matrix)

