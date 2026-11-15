from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):  
        c=Counter(s)
        for i in s:
            if c[i]==1:
                return s.index(i)
        return -1