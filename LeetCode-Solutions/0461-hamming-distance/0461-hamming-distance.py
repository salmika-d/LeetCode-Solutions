class Solution(object):
    def hammingDistance(self, x, y):
        x=bin(x)
        x=list(x[2:])
        y=bin(y)
        y=list(y[2:])
        if len(x)>len(y):
            for i in range(len(x)-len(y)):
                y.insert(0,'0')
        else:
            for i in range(len(y)-len(x)):
                x.insert(0,'0')    
        c=0
        for i in range(len(x)):
            if x[i] != y[i]:
                c+=1
        return c