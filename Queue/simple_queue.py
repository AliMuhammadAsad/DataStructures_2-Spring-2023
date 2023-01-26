## This file contains a simple implementation of Queue using lists in python - python does not have arrays so lists can be used as arrays ##
## Implementation done using classes ##

class Queue:
    def __init__(self)->None:
        self.queue = []
    
    def is_empty(self)->bool:
        return self.queue == []
    
    def enqueue(self, data)->None:
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty() == True:
            return "Cannot dequeue from an empty queue"
        return self.queue.pop(0)
    
    def front(self):
        if self.is_empty() == True:
            return "Queueu is empty"
        return self.queue[0]
