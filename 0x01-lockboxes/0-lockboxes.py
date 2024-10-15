#!/usr/bin/python3

"""A method with a number n locked boxes, each box is numbered from 0
each box contains keys to open other boxes
This method checks if all the boxes can be opened"""


def canUnlockAll(boxes):
    """checks if all boxes can be unlocked"""

    # initializes a set to keep track of opened boxes
    opened = set()
    # Start with the first box
    opened.add(0)

    # Initialize a list (acting as a queue) to explore boxes
    to_check = [0]

    while to_check:
        # Get the last box to check
        current_box = to_check.pop()

        # Check if we can access this box
        for key in boxes[current_box]:
            if key < len(boxes) and key not in opened:
                # Mark the box as opened
                opened.add(key)
                # Add it to the list to check later
                to_check.append(key)
    # Check if we've opened all boxes
    return len(opened) == len(boxes)
