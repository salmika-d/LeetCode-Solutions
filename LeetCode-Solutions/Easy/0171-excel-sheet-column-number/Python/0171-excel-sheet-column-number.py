class Solution(object):
    def titleToNumber(self, columnTitle):
        sum=0
        len1=len(columnTitle)
        for i in range(len1):
                sum+=((ord(columnTitle[i])-64)*(26**(len1-1-i)))
        return sum