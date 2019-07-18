class Node:
    def __init_(self, val):
        self.val = val
        self.l = None
        self.r = None
    def insert(self, val):
        if self.val == val:
            return False
        elif self.val > val:
            if self.l:
                return self.l.insert(val)
            else:
                self.l = Node(val)
                return True
        else:
            if self.r:
                return self.r.insert(val)
            else:
                self.r = Node(data)
                return True
            
            
class Tree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            b 

