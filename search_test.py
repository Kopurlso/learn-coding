"""
A collection of tests to test how search algorithms are running
"""

from binary_search import binary_search, binary_search_recursive

def test_binary_search():
    array = [0, 1, 2, 3, 4, 5]
    index = binary_search(array, 0)
    assert index == 0
    index = binary_search(array, 3)
    assert index == 3
    index = binary_search(array, -1)
    assert index == None
    index = binary_search(array, 1)
    assert index == 1
    index = binary_search(array, 2)
    assert index == 2
    index = binary_search(array, 5)
    assert index == 5

def test_binary_search_recursive():
    array = [0, 1, 2, 3, 4, 5]
    index = binary_search_recursive(array, 0)
    assert index == True
    index = binary_search_recursive(array, 3)
    assert index == True
    index = binary_search_recursive(array, -1)
    assert index == False
    index = binary_search_recursive(array, 1)
    assert index == True
    index = binary_search_recursive(array, 2)
    assert index == True
    index = binary_search_recursive(array, 5)
    assert index == True
