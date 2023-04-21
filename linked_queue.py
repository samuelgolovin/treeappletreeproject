class Queue:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return self.front is None

    def enqueue(self, data):
        """
        Adds an element to the rear of the queue.
        """
        new_node = Queue.Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        """
        Removes and returns the element from the front of the queue.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        if self.front == self.rear:
            self.rear = None
        front_node = self.front
        self.front = self.front.next
        self.size -= 1
        return front_node.data

    def peek(self):
        """
        Returns the element from the front of the queue without removing it.
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.front.data

    def get_size(self):
        """
        Returns the current size of the queue.
        """
        return self.size

    def view_all(self):
        """
        Returns a list containing all the elements in the queue.
        """
        elements = []
        current_node = self.front
        while current_node is not None:
            elements.append((current_node.data.element, current_node.data.label, current_node.data.quality))
            current_node = current_node.next
        return elements
