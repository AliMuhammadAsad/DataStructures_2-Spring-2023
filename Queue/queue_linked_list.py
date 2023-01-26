## This file contains an implementation of a Queue in python using singly linked lists ##

## We will need a node class using this implementation as in a linked list, each element also acts as a node that points towards the next node/element ##
## The implementation is done using the same basic concept as it was done in OOP in C++ ##

class Node:
    def __init__(self, data)->None:
        self.data = data
        self.next = None 

class Queue:
    def __init__(self)->None:
        self.front = None
        self.rear = None 
    
    def enqueue(self, data)->None:
        if self.rear is None:
            self.front = Node(data)
            self.rear = self.front
        else:
            self.rear.next = Node(data)
            self.rear = self.rear.next
    
    def dequeue(self):
        if self.head is None:
            return "Cannot dequeue from an empty queue"
        else:
            val = self.front.data
            self.front = self.front.next
            return val