"""
@desc: Linked List Implementation
"""

class Node:

    def __init__(self, data=None, next=None):

        self.data = data
        self.next = next
    

    def setData(self, data):
        self.data = data
    
    def getData(self):
        return self.data
    
    def setNext(self, next):
        self.next = next
    
    def getNext(self):
        return self.next

    def hasNext(self):

        if self.next is None:
            return False
        return True


class LinkedList:

    def __init__(self, node=None):

        self.length = 1
        self.head = node
        self.str_ptr = node
    

    def traverseList(self):

        str_ptr = self.str_ptr
        print("\n")
        while self.str_ptr is not None:
            print(f"{self.str_ptr.data}-> ", end="")
            self.str_ptr = self.str_ptr.next
        self.str_ptr = str_ptr
              
    def insetItem(self, item):
        if self.head is None:
            print("There is no any node in the linked list")
            return False
        node = Node(item)
        self.head.next = node
        self.head = node
        print(f"\n Item {item} has been inserted!")
        self.length +=1
   
    def deleteItem(self):
        pass
    

    def getListLength(self):
        return self.length


