# basic implementation of a stack (LIFO) with a few methods


class Stack:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def print(self):
        print(self.items)
