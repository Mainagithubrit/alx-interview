#!/usr/bin/python3
"""A 2D matrix being transposed and later reversed"""


def rotate_2d_matrix(matrix):
    """A function to transpose and reverse a matrix"""
    size = len(matrix)

    for i in range(size):
        for j in range(i + 1, size):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(size):
        matrix[i].reverse()
