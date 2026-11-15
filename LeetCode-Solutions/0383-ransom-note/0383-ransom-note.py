from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        if len(magazine)<len(ransomNote):
            return False
        else:
            c=Counter(magazine)
            for i in ransomNote:
                if c[i]>0:
                    c[i]-=1
                else:
                    return False
            return True