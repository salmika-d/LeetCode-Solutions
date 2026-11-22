class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s.count('b') > 0:
            new_s = s[(s.index('b'))::]
            if new_s.count('a') == 0:
                return True
            else:
                return False
        else:
            return True