class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        
        for i in range(len(s)):
            sum+=(27-(ord(s[i])-96))*(i+1)
        return sum