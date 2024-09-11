'Test file for HW2 test cases'
from hw1 import num_operations

def test_operations_valid():
    '''Test for valid mathematical operations'''
    assert num_operations(1,2) == [3, -1, 2, 0.5]
