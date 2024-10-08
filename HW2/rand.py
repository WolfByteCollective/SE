"""Helper function to generate random numbers"""

import secrets


def random_array(arr):
    """Function to generate random numbers"""
    for i, _ in enumerate(arr):
        # Generate secure random number between 1 and 20
        arr[i] = secrets.randbelow(20) + 1
    return arr
