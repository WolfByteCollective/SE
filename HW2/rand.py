""" HW2 rand.py"""
import subprocess

def random_array(arr):
    """Function random array"""
    shuffled_num = None
    for i, in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
