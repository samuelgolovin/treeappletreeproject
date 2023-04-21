class ArrayStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            # print("Stack is empty")
            return None
        return self.items.pop()

    def top(self):
        if self.is_empty():
            # print("Stack is empty")
            return None
        return self.items[-1]

    def get_size(self):
        return len(self.items)
