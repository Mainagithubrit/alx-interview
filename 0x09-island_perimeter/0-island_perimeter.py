#!/usr/bin/python3
"""An Island in 2D matrices"""

def island_perimeter(grid):
    """This program calculate the perimeter of an Island"""
    perimeter = 0

    rows = len(grid)
    colmn = len(grid[0])

    for r in range(rows):
        for c in range(colmn):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r -1][c] == 1:
                    perimeter -= 2

                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
