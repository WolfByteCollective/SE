from HW1 import NumOperations  
def test_operations_valid():
    assert NumOperations(1,2) == [3, -1, 2, 0.0]

def test_invalid_division():
    assert NumOperations(1, 4) == [5, -3, 4, 0.25]