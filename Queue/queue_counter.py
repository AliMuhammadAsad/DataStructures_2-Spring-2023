## This file contains an implementation of a Queue in python through the use of two counter variables inside the class ##

## The counter variables will be used to keep track of the elements in the queue - ie the front and rear of the queue ##

class Queue:
    def __init__(self)->None:
        self.queue = []
        front = 0; rear = 0