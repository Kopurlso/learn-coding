"""
A collection of tests to test how search algorithms are running
"""

from binary_search import binary_search

def test_binary_search():
    array = [0, 1, 2]
    index, count = binary_search(array, 0)
    assert index == 0
    assert count == 1

    array = [0,1,2,3,4,5]
    index, count = binary_search(array, 4)
    assert index == 4
    assert count == 2
