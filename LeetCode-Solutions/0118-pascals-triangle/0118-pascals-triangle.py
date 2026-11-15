class Solution(object):
    def generate(self, numRows):
        l=[]
        li=[1]
        l.append(li)
        for i in range (1,numRows):
            li=[]
            li.insert(0,1)
            li.insert(i,1)
            for j in range (1,i):
                li.insert(j,(l[i-1][j-1]+l[i-1][j]))
            l.append(li)
        return l