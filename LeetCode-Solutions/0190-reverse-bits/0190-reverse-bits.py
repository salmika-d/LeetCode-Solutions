class Solution(object):
    def reverseBits(self, n):
        b=""
        while(n!=0):
            b=b+str(n%2)
            n=n//2
        if(len(b)<32):
            for i in range(32-len(b)):
                b=b+'0'
        n=int(b,2)
        return n