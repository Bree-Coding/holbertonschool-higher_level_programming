#!/usr/bin/python3

def matrix_divided(matrix, div):
    """"This function divides all elements of a matrix by an integer.
    All element should be a list of integers or floats.
    The function returns a new matrix.
    An error message is displayed if the matrix is not a list of lists of integers or floats.
    An error message is also displayed if the matrix has different sizes.
    An error message is also displayed if div is not an integer or a float or if div is equal to zero.
    Matrix is a list of lists of integers or floats.
    div is a number (integer or float)."""

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]
