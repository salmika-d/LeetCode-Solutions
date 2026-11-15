class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)==len(t):
            for i in range(len(s)):
                if s.count(s[i])!=t.count(t[i]):
                    return False
                if len(s)<25:
                  for j in range(i,len(s)):
                    if (s[i]==s[j] and t[i]!=t[j]) or (s[i]!=s[j] and t[i]==t[j]):
                        return False
            return True
        else:
            return False      