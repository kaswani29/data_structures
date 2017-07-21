class LinekedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None


def cyclic(head):
    current = head
    slow_runner = head
    fast_runner = head

    while (fast_runner is not None and fast_runner.next is not None):

        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        if slow_runner == fast_runner:
            return True

    return False