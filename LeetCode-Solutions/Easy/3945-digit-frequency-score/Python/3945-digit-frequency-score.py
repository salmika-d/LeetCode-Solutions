class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        freq=0
        d=[0]*10

        while(n!=0):
            digit=n%10
            n=n//10
            d[digit] = d[digit]+1

        for i in range(10):
            freq+=d[i]*i

        return freq