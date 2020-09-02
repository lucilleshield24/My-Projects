class Queue:
    def __init__(self):
        self.list = []
    def push(self,x):
        self.list.append(x)
    def sort(self):
        self.list.sort(key= lambda x: x['age'], reverse=True)
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
        
def test():
    q = Queue()
    v1 = {"first":"alan", "last":"shield", "age":13}
    q.push(v1)
    v2 = {"first":"luci", "last":"shield", "age":18}
    q.push(v2)
    v3 = {"first":"helena", "last":"shield", "age":21}
    q.push(v3)
    
    highest = q.pop()
    if highest['age'] == v3['age']:
        print("yay!")
    else:
        print("booo!")

