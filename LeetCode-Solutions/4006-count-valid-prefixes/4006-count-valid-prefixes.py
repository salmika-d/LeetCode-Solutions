class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        z=0
        l=0
        c=0
        for i in range(len(s)):
            if s[i]=='0':
                z+=1
            else:
                l+=1
            if abs(z-l)<=1:
                c+=1
        return c