class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

a = LinkedListNode(1)
b = LinkedListNode(2)
c = LinkedListNode(3)

a.next = b
b.next = c


def reverse(a):
    current = a

    while (current):
        b = current.next
        temp = b.next
        current = b.next
        current = b
