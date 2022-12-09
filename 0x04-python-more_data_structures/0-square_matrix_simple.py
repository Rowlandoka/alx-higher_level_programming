#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squareMatrix = []
    for col in matrix:
        result = list(map(lambda x: x**2, col))
        squareMatrix.append(result)
    return squareMatrix
   