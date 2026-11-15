from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        c=Counter(s)
        c1=Counter(t)
        for i in t:
            if i not in s or c[i]!=c1[i]:
                return i 