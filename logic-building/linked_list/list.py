"""
"""

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:

    def add_node(self, val, list=None):
        if list is None:
            return ListNode(val)
        node = ListNode(val)
        list.next = node
        return node
    
    def read_list(self, list):
        if list is None:
            return
        print(list.val)
        return self.read_list(list.next)

if __name__ == '__main__':
    list = LinkedList()
    data = [1,2,3,4,5]
    node = None
    start = None
    for d in data:
        if node is None:
            start = list.add_node(d)
            node = start
        node = list.add_node(d, node)
        # print(node)
    
    list.read_list(start)
        