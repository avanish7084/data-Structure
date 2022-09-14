
class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    # addNode() will add a node to the list
    def addNode(self,data):

        newNode=Node(data) # First we will be create newnode with the help of class Node

        if self.head==None: # if head will be empty

            self.head=newNode  # if list will be empty then head will be point to newNode

            self.tail=newNode  # and also tail will be poin to newnode

            self.head.prev=None
            self.tail.next=None
        else:
            self.tail.next=newNode   # newNode will be added after tail such that tail's next will point to newNode

            newNode.prev=self.tail  # newNode's previous will point to tail

            self.tail=newNode        # now tail node will be become to newnode

            self.tail.next= None     # after all process tail next will be point to None
    def printdb_linkedlist(self):
        curr=self.head
        while curr.next!=None:
            print(curr.data,end="->")
            curr=curr.next
        print(curr.data)


dblinked=Linkedlist()
dblinked.addNode(2)
dblinked.addNode(3)
dblinked.addNode(5)
dblinked.addNode(8)
dblinked.printdb_linkedlist()
