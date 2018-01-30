# This is a class implemented for queue data structure

class Q(object):
    def __init__(self):
        self.arr = []
        return
    
    def enq(self, elem):
        self.arr.insert(0, elem)
        return
    
    def deq(self):
        return self.arr.pop()
    
    def peek(self):
        return self.arr[-1]
    
    def isEmpty(self):
        return self.arr == []
    
    def size(self):
        return len(self.arr)
    