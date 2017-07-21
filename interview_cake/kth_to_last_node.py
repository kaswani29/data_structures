from collections import deque
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None

a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

kth_to_last_node(2, a)

def kth_to_last_node(value,head):
   store =  deque([0]*value)

   current = head
   while(current):
       store.appendleft(current.value)
       store.pop()
       current = current.next

    return store.pop()



