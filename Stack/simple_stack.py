## This file contains a simple implementation of a Stack using lists in python - python does not have arrays so lists can be used as arrays. ##

## The implementation is done using classes ##

class Stack:
    def __init__(self)->None:
        self.stack = []

    def is_empty(self):
        return self.stack == []
    
    def push(self, data)->None:
        self.stack.append(data)
    
    def pop(self):
        if self.is_empty() == True:
            return("Cannot pop from an empty stack")
        return self.stack.pop()
    
    def top(self):
        if self.is_empty() == True:
            return("Cannot show any value from an empty stack")
        return self.stack[-1]
    

## Testing for stack:
# s = Stack()
# print(s.pop())
# print(s.pop())
# for i in range(10):
#     s.push(i)

# while s.is_empty() == False:
#     print(s.pop())