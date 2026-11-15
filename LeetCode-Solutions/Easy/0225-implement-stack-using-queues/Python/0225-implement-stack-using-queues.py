class MyStack(object):

    def __init__(self):
        self.stack = []
        self.topp = -1

    def push(self, x):
        self.topp = self.topp + 1
        self.stack.append(x)
        
    def pop(self):
        c = self.stack.pop()
        self.topp = self.topp - 1
        return c

    def top(self):
        return self.stack[self.topp]
        
    def empty(self):
        if self.topp == -1:
            return True
        else:
            return False
