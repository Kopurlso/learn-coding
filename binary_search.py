import numpy as np

def binary_search_recursive(array, min, max, value, count):
    """
    Performs a binary search through the array for a given value. Recursive
    method assuming list is already sorted.
    ===
    :count: int used for testing(keeps track of how many times the function is called)
    :array: [int]
    :value: int
    :rytpe: int (location of value, will return None if value is not found)
    ===
    """
    mid = int(min + (max-min)/2)
    if (mid == min) | (mid == max):
        return -1, count + 1
    if array[mid] == value:
        return mid, count + 1
    elif array[mid] < value:
        binary_search(array, mid, max, value, count)
    elif array[mid] > value:
        binary_search(array, min, mid, value, count)

def binary_search(array, value):
    """
    Performs a binary search through the array for a given value. Nonrecursive
    method assuming list is already sorted.
    ===
    :count: int used for testing(keeps track of how many times the function is called)
    :array: [int]
    :value: int
    :rytpe: int (location of value, will return None if value is not found)
    ===
    """
    low = 0
    high = len(array)-1
    count = 0
    while True:
        mid = int(low + np.ceil((high - low)/2))
        print("Mid is", mid)
        if array[mid] == value:
            return mid, count
        elif array[mid] < value:
            if mid == low:
                break
            low = mid
            count += 1
        else:
            if high == mid:
                break
            high = mid
            count += 1
            print(low)
            print(high)
    return None, count
