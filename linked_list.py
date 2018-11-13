
"""
Create a funtional linked list
"""
class Node():
    """
    The bread and butter of linked lists. Each Node consists of a head (value)
    as well as a tail (pointer) to another Node.
    """
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def next_is_empty(self):
        if self.tail is None:
            return True
        return False

class Linked_List():
    """
    Data structure that heads a list of connected Nodes (see above). Has
    functionality much like a normal array.
    """
    def __init__(self):
        self.head = None

    # print out each value of the linked list
    def show(self):
        temp = self.head
        while temp.next_is_empty() == False:
            print(temp.head)
            temp = temp.tail
        print(temp.head)

    # return size of linked list
    def size(self):
        if self.empty():
            return 0
        count = 1
        temp = self.head
        while temp.next_is_empty() != True:
            count += 1
            temp = temp.tail
        return count

    # return boolean whether linked list is empty or not
    def empty(self):
        if self.head is None:
            return True
        return False

    # return value at a given index
    def value_at(self, index):
        if index >= (self.size()) or not isinstance(index, int) or index < 0:
            return "IndexError: Index is too large or incorrect. Should be an integer less than size of linkedlist"
        temp = self.head
        while index != 0:
            temp = temp.tail
            index -= 1
        return temp.head

    # adds a value to the front of the linked list
    def push_front(self, value):
        temp_node = Node(value, self.head)
        self.head = temp_node

    # returns the head of the linked list and removes it
    def pop_front(self):
        front = self.head.head
        self.head = self.head.tail
        return front

    # adds a value to the back of the linked list
    def push_back(self, value):
        temp_node = self.head
        while temp_node.next_is_empty() == False:
            temp_node = temp_node.tail
        temp_node.tail = Node(value)
        pass

    # returns the tail of the linked list and removes it
    def pop_back(self):
        temp_node = self.head
        prev_node = None
        while temp_node.next_is_empty() == False:
            prev_node = temp_node
            temp_node = temp_node.tail
        prev_node.tail = None
        return temp_node.head

    # return the head value
    def front(self):
        return self.head.head

    # return the tail value of the linked list
    def back(self):
        temp_node = self.head
        while temp_node.next_is_empty() == False:
            temp_node = temp_node.tail
        return temp_node.head

    # insert a value at a given index_col
    def insert_at(self, index, value):
        if index == 0:
            self.head = Node(value, self.head)
            return
        temp_node = self.head
        prev_node = None
        while index != 0:
            index -= 1
            prev_node = temp_node
            temp_node = temp_node.tail
        prev_node.tail = Node(value, temp_node)

    # removes node at given index
    def remove(self, index):
        if index == 0:
            self.pop_front()
            return
        elif index == self.size() - 1:
            self.pop_back()
            return
        temp_node = self.head
        prev_node = None
        while index != 0:
            index -= 1
            prev_node = temp_node
            temp_node = temp_node.tail
        prev_node.tail = prev_node.tail.tail

    # returns the value of the node nth from the back
    def value_n_from_end(self, n):
        return self.value_at(self.size() - 1 - n)

    # reverses the linked lists
    def reverse(self):
        reversed = Linked_List()
        reversed.head = Node(self.back())
        temp_node = reversed.head
        for x in range(self.size() - 1):
            temp_node.tail = Node(self.value_n_from_end(x + 1))
            temp_node = temp_node.tail
        return reversed

    # removes first occurence of value
    def remove_value(self, value):
        temp_node = self.head
        index = 0
        while temp_node.next_is_empty() == False:
            if temp_node.head == value:
                self.remove(index)
                return
            index += 1
            temp_node = temp_node.tail
