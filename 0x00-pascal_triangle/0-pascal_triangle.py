#!/usr/bin/python3
"""A python function for pascals triangle"""


def pascal_triangle(n):
    """In this function we are creating Pascals Triangle
    Parameters:
        x: represents a row
    Returns:
        pascals_triangle (list): which is an empty list"""

    # Create an empty list to hold the triangle
    pascals_triangle = []
    if n <= 0:
        return pascals_triangle

    for x in range(n):
        # Start each row with a list
        current_row = []
        # The first number in every row is always 1
        current_row.append(1)
        # Fill in the middle numbers
        if x > 1:
            # Only calculate middle numbers if it's not the first two rows
            last_row = pascals_triangle[x - 1]
            for j in range(1, x):
                # Each number is the sum of the two numbers above it
                current_row.append(last_row[j - 1] + last_row[j])
    # The last number in every row is always 1
        current_row.append(1)
    # Add the current row to the triangle
        pascals_triangle.append(current_row)

    return pascals_triangle
