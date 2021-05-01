"""

"""

class Node:

    def __init__(self, value):

        self.data = value
        self.next = None



class Queue:

    def __init__(self):
        # add element to queue
        self.rear = None
        # delete element from queue
        self.front = None
    

    def insert(self):
        value = input("enter the value to insert in queue")
        node = Node(value)

        if self.rear is None:
            self.rear = node
            self.front = node
        else:
            node.next = self.rear
            self.rear = node
    
    def traversal(self):
        temp  = self.rear
        while True:

            print(f"{self.rear.data} ->", end="")

            if self.rear.next == None:
                print("\n")
                break

            self.rear = self.rear.next
        
        self.rear = temp
    

    def get_front(self):
        return self.front

