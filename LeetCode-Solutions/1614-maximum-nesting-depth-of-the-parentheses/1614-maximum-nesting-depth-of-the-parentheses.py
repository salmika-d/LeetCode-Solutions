class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        i=0
        res=0
        c=0
        while (i < len(s)):
        
            if s[i] == '(':
                while (i < len(s) and s[i] != ')'):
                    if s[i] == '(':
                        c += 1
                    i += 1
                    
            if m < c :
                m=c
            
            while (i < len(s) and s[i] != '('):
                if s[i] == ')':
                   c-=1 
                i+=1

        return m 
            
        