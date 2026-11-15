class Solution(object):
    def wordPattern(self, pattern, s):
        s=s.split()
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)-1):
            for j in range(i+1,len(pattern)):
                if pattern[i]==pattern[j] and s[i]!=s[j]:
                    return False
                if pattern[i]!=pattern[j] and s[i]==s[j]:
                    return False
        return True
        