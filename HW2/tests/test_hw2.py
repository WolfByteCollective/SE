'Test file for HW2 test cases'
from hw2_debugging import merge_sort

def test_sorting_valid_odd():
    '''Test for successful sorting'''
    assert merge_sort([1,6,7,5,4,2,3]) == [1,2,3,4,5,6,7]

def test_sorting_valid_even():
    '''Test for successful sorting for even number of elements'''
    assert merge_sort([1,6,7,8,5,4,2,3]) == [1,2,3,4,5,6,7,8]

def test_sorting_single_element():
    '''Test for successful sorting'''
    assert merge_sort([1]) == []
