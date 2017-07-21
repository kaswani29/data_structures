
class queue (object):

    def __init__(self):
        self.stack1 = []
        self.stack2 = []


    def enqueue(self, value):
        self.stack1.append(value)

    def dequeue(self):
        if len(self.stack2)== 0:
            while (len(self.stack1)>0):
                self.stack2.append(self.stack1.pop())
        if len(self.stack2)==0:
            print ("Nothing to dequeue")
            return None
        return self.stack2.pop()

    def check(self):
        print (self.stack1)
        print (self.stack2)
