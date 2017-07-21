class Stack:
    # initialize an empty list
    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        # if the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None
        return self.items.pop()

    # see what the last item is
    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class MaxStack():
    def __init__(self):
        self.container = Stack()
        self.max_container = Stack


    def push1(self, item):
        if len(self.max_container)>0:
           if self.max_container[-1] < item:
               self.max_container.append(item)
        else:
            self.max_container.append(item)
        self.container.push(item)

    def pop2(self):
        out = self.container.pop()

        if out in self.max_container:

        if len(self.max_container)>0:
           if self.max_container[-1] < item:
               self.max_container.append(item)
        else:
            self.max_container.append(item)
        self.container.push(item)




