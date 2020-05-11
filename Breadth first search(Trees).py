from _collections import deque
from queue import Queue


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_left_child(self):
        return self.left

    def set_left_child(self, left):
        self.left = left

    def get_right_child(self):
        return self.right

    def set_right_child(self, right):
        self.right = right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # Define __repr__ to decide what a print statement displays for a Node
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


# Defining Tree class
class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


# Adding nodes as children
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        if len(self.q) > 0:
            s = "<enqueue here>\n_____________________\n"
            s += "\n_____________________\n".join([str(item) for item in self.q])
            s += "\n_____________________\n<dequeue here>"
            return s
        else:
            return "<queue is empty>"


q = Queue()
q.enq("apple")
q.enq("banana")
q.enq("cherry")
print(q)
