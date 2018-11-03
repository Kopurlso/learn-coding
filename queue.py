"""
Create a working queue
"""

class Queue():
    """
    Implementing a queue using an array of fixed size with pointers
    """
    def __init__(self, size):
        self.read = 0
        self.queue = [None]*size
        self.write = 0
        self.size = size

    def show(self):
        for x in self.queue:
            print(x)

    # adds an element to the queue
    def enqueue(self, value):
        if self.full():
            return "Queue is full."
        self.queue[self.write] = value
        if self.write == self.size - 1:
            self.write = 0
        else:
            self.write = self.write + 1

    # reads an element on a FIFO basis
    def dequeue(self):
        if self.empty():
            return "Queue is empty"
        value = self.queue[self.read]
        if self.read == self.size - 1:
            self.read = 0
        else:
            self.read = self.read + 1
        return value

    # checks if queue is full
    def full(self):
        write = self.write
        if self.write == self.size - 1:
            if self.read == 0:
                return True
        if self.write + 1 == self.read:
            return True
        return False

    # checks if queue is empty
    def empty(self):
        if self.read == self.write:
            return True
        return False
