# Node structure
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


# Stack class
class myStack:
    def __init__(self):
        # initially stack is empty
        self.top = None
        self.stack_size = None
    
    def push(self, value):
        node = Node(value)
        
        if self.top is None:
            self.top = node
            self.stack_size = 1
        else:
            current = node.next
            lastnode = self.top
            self.top = node
            self.top.next = lastnode
            self.top = node
            self.stack_size+= 1

    def print_stack(self) :
        current = self.top
        while current is not None:
            print (current.data)
            current = current.next
    

stack = myStack()
stack.insert(10)
stack.insert(20)
stack.insert(30)

stack.print_stack()