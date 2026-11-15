class Solution(object):
    def findComplement(self, num):
       cres=0
       bres=bin(num)[2:]
       n=len(bres)-1
       for i in bres:
        if i=='0':
            cres+=2**n
        n-=1
       return cres