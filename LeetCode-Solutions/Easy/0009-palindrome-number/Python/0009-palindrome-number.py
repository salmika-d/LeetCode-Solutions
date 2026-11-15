class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            x=str(x)
            s=x[::-1]
            if(x==s):
                return True
            else:
                return False
