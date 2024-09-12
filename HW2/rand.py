""" This file contains the helper function to generate random numbers in a given range"""

import secrets
def random_array(arr):
    """Function to generate random numbers"""
    for i, _ in enumerate(arr):
        arr[i] = secrets.randbelow(20) + 1  # Generate secure random number between 1 and 20
    return arr
