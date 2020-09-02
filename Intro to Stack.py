class StackTask:
    def __init__(self):
        self.stack = []
    
    def push(self, a):
        self.stack.append(a)
        
    def pop(self):
        if len(self.stack) == 0:
            return ["There are no items in this stack."]
        else:
            b = self.stack[-1]
            del self.stack[-1]
            return b
         
    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
