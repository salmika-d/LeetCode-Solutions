class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        sum=0
        if n-k>0:
            i=n-k
        else:
            i=1
        for x in range(i,n+k+1):
            if abs(n-x) <= k and (n & x)==0:
                sum+=x
        return sum