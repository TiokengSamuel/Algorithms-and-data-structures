from pip._vendor.progress.counter import Stack


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
        return self.value

    def set_left_child(self, node):
        self.left = node

    def get_right_child(self):
        return self.value

    def set_right_child(self, node):
        self.right = node

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
class Tree(object):
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


# Adding nodes as children
tree = Tree("apple")
tree.get_root().set_left_child(Node("banana"))
tree.get_root().set_right_child(Node("cherry"))
tree.get_root().get_left_child().set_left_child(Node("dates"))

# Driver code
node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")
node0.set_left_child(node1)
node0.set_right_child(node2)
print(f"""
node 0: {node0.value}
node 0 left child: {node0.left.value}
node 0 right child: {node0.right.value}
""")


# ********Making visual tree in code**********
visit_order = list()
stack = Stack()

#start at the root node, visit it and then add it to the stack
node = Tree.get_root()
stack.push(node)

print(f"""
visit_order {visit_order}
stack: {stack}
""")

def pre_order_with_stack_buggy(tree):
    visit_order = list()
    stack = Stack()
    node = tree.get_root()
    stack.push(node)
    node = stack.top()
    visit_order.append(node.get_value())
    count = 0
    loop_limit = 7
    while(node and count < loop_limit):
        print(f"""
loop count: {count}
current node: {node}
stack:
{stack}
""")
        count +=1
        if node.has_left_child():
            node = node.get_left_child()
            stack.push(node)
            #using top() is redundant, but added for clarity
            node = stack.top()
            visit_order.append(node.get_value())

        elif node.has_right_child():
            node = node.get_right_child()
            stack.push(node)
            node = stack.top()
            visit_order.append(node.get_value())

        else:
            stack.pop()
            if not stack.is_empty():
                node = stack.top()
            else:
                node = None

     return visit_order