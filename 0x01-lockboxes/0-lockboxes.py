#!/usr/bin/python3
"""lockboxes module"""


def canUnlockAll(boxes):
    """
    Defines a function to unlock boxes
       Args:
          boxes: boxes to be unlocked
       Retuns:True if all boxes can be opened, else return False
    """

    # Number of boxes
    n = len(boxes)

    # Create a set to track which boxes are unlocked
    unlocked = set()
    unlocked.add(0)  # Box 0 is unlocked by default

    # Stack (DFS) or queue (BFS) to track the boxes we can explore
    stack = [0]

    # While there are boxes to explore
    while stack:
        box = stack.pop()

        # Go through all the keys in the current box
        for key in boxes[box]:
            # If the key is for a valid box and it's not already unlocked
            if key < n and key not in unlocked:
                unlocked.add(key)  # Unlock the box
                stack.append(key)  # Add the box to explore further
    return len(unlocked) == n
