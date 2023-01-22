## This file contains an implementation of a stack in python using singly linked lists ##

## We will need a node class using this implementation as in a linked list, each element also acts as a node that points towards the next node/element ##
## The implementation is done using the same basic concept as it was done in OOP in C++ ##

class Node:
    def __init__(self, data)->None:
        self.data = data
        self.next = None 

class Stack:
    def __init__(self)->None:
        self.head = Node("head")
        self.size = 0

    def is_empty(self)->bool:
        return self.size == 0

    def push(self, element)->None:
        node = Node(element)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
    
    def pop(self):
        if self.is_empty() == True:
            return "Cannot pop from an empty stack"
        val = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return val.data
    
    def top(self):
        if self.is_empty() == True:
            return "Stack is empty"
        return self.head.next.data
    
    def __str__(self): #String representation of the stack
        val = self.head.next
        out = ""
        while val:
            out += str(val.data) + "->"
            val = val.next
        return out[:-2]

## Testing for Stack
# stack = Stack()
# for i in range(1,11):
#     stack.push(i)

# print(f"Stack: {stack}")

# for i in range(6):
#     print(f"Popped: {stack.pop()}")

# print(f"Stack: {stack}")
