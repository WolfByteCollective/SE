from HW2.hw2_debugging import merge_sort

def test_sorting_valid():
    assert merge_sort([1,6,7,5,4,2,3]) == [1,2,3,4,5,6,7]