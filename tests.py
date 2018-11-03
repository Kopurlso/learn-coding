"""
A collection of tests to ensure classes are implemented and functioning correctly
"""

from linked_list import Node, Linked_List

def test_linked_list():
    """
    Code to test each part of the linked list class
    """
    # empty()
    ll = Linked_List()
    assert ll.empty() == True
    ll.head = Node(3)
    assert ll.empty() == False

    # next_is_empty()
    assert ll.head.next_is_empty() == True
    ll.head.tail = Node(4)
    assert ll.head.next_is_empty() == False

    # size()
    ll.head.tail.tail = Node(5)
    assert ll.size() == 3
    assert Linked_List().size() == 0
    size_one = Linked_List()
    size_one.head = Node(18)
    assert size_one.size() == 1

    # value_at()
    assert ll.value_at(0) == 3
    assert ll.value_at(1) == 4
    assert ll.value_at(2) == 5
    assert ll.value_at(3) == "IndexError: Index is too large or incorrect. Should be an integer less than size of linkedlist"

    # push_front()
    ll.push_front(2)
    assert ll.value_at(0) == 2
    assert ll.value_at(1) == 3
    assert ll.value_at(2) == 4
    assert ll.value_at(3) == 5
    assert ll.size() == 4

    # pop_front()
    front_value = ll.pop_front()
    assert front_value == 2
    assert ll.size() == 3
    assert ll.value_at(0) == 3

    # push_back()
    ll.push_back(6)
    assert ll.size() == 4
    assert ll.value_at(3) == 6

    # pop_back()
    back_value = ll.pop_back()
    assert ll.size() == 3
    assert back_value == 6

    # front()
    front_value = ll.front()
    assert front_value == 3
    assert ll.size() == 3

    # back()
    back_value = ll.back()
    assert back_value == 5
    assert ll.size() == 3

    # insert_at()
    ll.insert_at(0, 2)
    assert ll.size() == 4
    assert ll.value_at(0) == 2
    ll.insert_at(1, 2.5)
    assert ll.size() == 5
    assert ll.value_at(1) == 2.5
    assert ll.value_at(2) == 3

    # erase()
    ll.remove(0)
    assert ll.size() == 4
    assert ll.value_at(0) == 2.5
    ll.remove(1)
    assert ll.size() == 3
    assert ll.value_at(1) == 4

    # value_n_from_end()
    n = ll.value_n_from_end(0)
    assert n == 5
    assert ll.size() == 3

    # reverse()
    reversed = ll.reverse()
    assert reversed.size() == 3
    assert reversed.value_at(0) == 5
    assert reversed.value_at(1) == 4
    assert reversed.value_at(2) == 2.5

    # remove_value(value)
    reversed.remove_value(4)
    assert reversed.size() == 2
    assert reversed.value_at(0) == 5
    assert reversed.value_at(1) == 2.5
