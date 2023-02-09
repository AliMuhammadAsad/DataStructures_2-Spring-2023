class Node:
    def __init__(self, data):
        self.data = data; self.next = None; self.prev = None
    
class DoublyLinkedList:
    def __init__(self):
        self.first = None
    
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.first #new node is made to point next to first node
        # new_node.prev = None
        if self.first is not None: #Change previous of first node to new node
            self.first.prev = new_node
        self.first = new_node #move the first to point to the new node
    
    def insert_after(self, prev_node, data):
        if prev_node is None:
            return "Your previous node doesn't exists"
        new_node = Node(data)
        new_node.next = prev_node.next #next of new node is made previous node's next so both point to the next node
        prev_node.next = new_node #previous node's next is now made to point to our new node
        new_node.prev = prev_node #new node's is also made to point to the previous node
        if new_node.next is not None: #if the next node is not none and exists, it is made to also point to our new node
            new_node.next.prev = new_node
    
    def insert_at_rear(self, data):
        new_node = Node(data)
        if self.first is None:
            self.first = new_node
            return
        temp = self.first #storing head node in a temporary variable for traversal
        while temp.next is not None: #traversing to the end of doubly linked list
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
        # return
    
    def remove_node(self, node):
        if self.first is None or node is None:
            return "Cannot delete from an empty linked list"
        if self.first == node: #If first is that node, first is now the next node
            self.first = node.next
            node.next.prev = self.first
        if node.next is not None: #If node is not the last element, then the previous node now points to the next node
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

        
        