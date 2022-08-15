# implementation and traverse the Linkedlist

class Node:
    # creating the node
    def __init__(self,data):
        self.data=data
        self.next=None


class Linkedlist:
    def __init__(self):
        self.head=None

    # insertion at beginning
    
    def insertion_beginning(self,key):
        new_node=Node(key)
        new_node.next=self.head
        self.head=new_node

    # insertion after node
    
    def insertion_after_node(self,key,node_after):
        p=self.head
        if p is None:
            print("The Node can not be inserted")
            return
        else:
            while p.data!=node_after:
                p=p.next
                if p is None:
                    print("The Node can not be inserted")
                    return
            new_node=Node(key)
            new_node.next=p.next
            p.next=new_node

    # insertion at the end
    
    def insertion_end(self,key):
        p=self.head
        if p is None:
            new_node=Node(key)
            self.head=new_node
        else:
            while p.next != None:
                p = p.next
            new_node = Node(key)
            p.next = new_node


    # print linkedlist
    
    def print_Linkedlist(self):
        p=self.head
        while p is not None:
            print(p.data,end=" -> ")
            p=p.next
        print("None")


if __name__=='__main__':
    list=Linkedlist()
    list.insertion_end(5)
    list.insertion_beginning(6)
    list.insertion_end(10)
    list.insertion_beginning(15)
    list.insertion_after_node(9,5)
    list.print_Linkedlist()
    
