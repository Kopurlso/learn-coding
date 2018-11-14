def binary_search_recursive(array, value):
    """
    Performs a binary search through the array for a given value. Recursive
    method assuming list is already sorted.
    ===
    :count: int used for testing(keeps track of how many times the function is called)
    :array: [int]
    :value: int
    :rytpe: bool (True if value is found)
    ===
    """
    if len(array) == 0:
        return False
    midpoint = round(len(array)/2)
    if array[midpoint] == value:
        return True
    elif array[midpoint] < value:
        return binary_search_recursive(array[midpoint + 1:], value)
    else:
        return binary_search_recursive(array[:midpoint], value)


def binary_search(array, value):
    """
    Performs a binary search through the array for a given value. Nonrecursive
    method assuming list is already sorted.
    ===
    :array: [int]
    :value: int
    :rytpe: int (location of value, will return None if value is not found)
    ===
    """
    low = 0
    high = len(array) - 1
    found = False
    while low <= high and not found:
        midpoint = round(low + (high - low)/2)
        if array[midpoint] == value:
            return midpoint
        elif array[midpoint] < value:
            low = midpoint + 1
        else:
            high = midpoint - 1
    return None
