"""
@Author: Mr-Black
@Description: Implementation of stack [Last-In-First-Out]
@Operation: 
    - Insertion
    - Deletion
    - Seaching 
"""

class Stack:

    def __init__(self):

        self.stack = []


    def options_menu(self):

        print(f"List of operation that you want to perform on stack.\n")

        print(f"1- Insertion")

        print(f"2- Deletion")

        print(f"3- Searching \n")
    

    def insertion(self, kth=0):

        val= int(input("Enter the value :"))
        self.stack.append(val)
    
    def delete(self, kth=0):

        if len(self.stack):
            print(f"Top {kth} element has been deleted")
            self.stack.pop()
        else:
            print(f"list are empty")
    
    def read(self):

        print(f"list are : {self.stack}")




