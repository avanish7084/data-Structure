
class Queue:
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

    def enqueue_operation(self,x):
        while len(self.stack1)!=0:
            d=self.stack1.pop()
            self.stack2.append(d)

        self.stack1.append(x)

        while len(self.stack2)!=0:
            d=self.stack2.pop()
            self.stack1.append(d)

    def dequeue_operation(self):
        if len(self.stack1)==0:
            print("Queue is empty")
        while len(self.stack1)!=0:
            d=self.stack1.pop()
            print(d)


q=Queue()
q.enqueue_operation(6)
q.enqueue_operation(5)
q.dequeue_operation()
q.dequeue_operation()
