'Test file for HW2 test cases'
from hw2_debugging import merge_sort

def test_sorting_valid():
    '''Test for successful sorting'''
    assert merge_sort([1,6,7,5,4,2,3]) == [1,2,3,4,5,6,7]
