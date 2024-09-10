""" HW2 rand.py"""

import secrets

def random_array(arr):
    """Function to shuffle array with cryptographically secure random numbers"""
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1  # Generate secure random number between 1 and 20
    return arr
