from node import Node


class LinkedList(object):
    def __init__(self):
        self.head = None

    def set_head(self, head_node):
        self.head = head_node

    def get_head(self):
        return self.head.get_data()

    def get_back(self):
        current = self.head
        back_data = self.head.get_data()
        while current:
            back_data = current.get_data()
            current = current.get_next()
        return back_data

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.get_next()
        return count

    def empty(self):
        if len(self) == 0:
            return True
        else:
            return False

    def push_head(self, new_node):
        node = Node(new_node)
        node.set_next(self.head)
        self.set_head(node)

    def push_back(self, new_node):
        node = Node(new_node)
        current = self.head
        if not current:
            self.head = node
            return

        while current.get_next():
            current = current.get_next()

        current.set_next(node)

    def value_at(self, index):
        count = 0
        current = self.head
        index_data = self.head
        while count <= index:
            count += 1
            index_data = current.get_data()
            current = current.get_next()
        return index_data

    def pop_front(self):
        current_head = self.head
        new_head = current_head.get_next()
        self.set_head(new_head)
