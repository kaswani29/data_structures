class LinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        pass



a = LinkedList(4)
b = LinkedList(5)
c = LinkedList(6)

b = a.next
c = b.next