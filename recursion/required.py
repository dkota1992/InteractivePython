class Stack(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self,value):
        self.items.append(value)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[self.size()-1]
    
    def size(self):
        return len(self.items)