class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

node1 = LinkedList("3")
node2 = LinkedList("7")
node3 = LinkedList("10")
node4 = LinkedList("27")

node1.nextNode = node2
node2.nextNode = node3
node3.nextNode = node4

currentNode = node1
while True:
    print(currentNode.value, "->", end=' ')
    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode

### Linked list with OOP

class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class linkedlist:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return

        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode


    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->", end=' ')
            currentNode = currentNode.nextNode
            print("None")

ll = linkedlist()
ll.printLinkedList()
ll.insert("3")
ll.printLinkedList()
ll.insert("44")
ll.printLinkedList()
ll.insert("55")


