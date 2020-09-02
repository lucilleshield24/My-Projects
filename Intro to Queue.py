class Queue:
    def __init__(self):
        self.list = []
    def push(self,x):
        self.list.append(x)
    def sort(self):
        self.list.sort(key=lambda x: x.priority, reverse=True)
    def pop(self):
        if self.is_empty():
            return None
        else:
            self.sort()
            return self.list.pop(0)
    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

class Item:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        
def test():
    q = Queue()
    v1 = Item(1, 2)
    q.push(v1)
    v2 = Item(2, 3)
    q.push(v2)
    v3 = Item(3, 4)
    q.push(v3)
    
    highest = q.pop()
    if highest.value == v3.value:
        print("yay!")
    else:
        print("booo!")
        
        
    