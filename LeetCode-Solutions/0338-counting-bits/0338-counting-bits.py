class Solution(object):
    def countBits(self, n):
        ans=[]
        b=""
        for i in range(n+1):
            b=bin(i)
            ans.append(b.count('1'))        
        return ans