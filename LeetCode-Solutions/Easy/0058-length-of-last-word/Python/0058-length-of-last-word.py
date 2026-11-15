class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip()
        c=0
        i=len(s)-1
        while(s[i]!=' ' and i>-1):
            c=c+1
            i=i-1
        return c