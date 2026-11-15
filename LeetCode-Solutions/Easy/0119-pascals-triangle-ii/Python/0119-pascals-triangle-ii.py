class Solution(object):
    def getRow(self, rowIndex):
        l=[1]
        for i in range (1,rowIndex+1):
            li=[]
            li.insert(0,1)
            li.insert(i,1)
            for j in range (1,i):
                li.insert(j,(l[j-1]+l[j]))
            l=li
        return l