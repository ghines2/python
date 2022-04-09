class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node("First Node")
head.next = Node("Next Node")
head.next.next = Node("3rd Node")

