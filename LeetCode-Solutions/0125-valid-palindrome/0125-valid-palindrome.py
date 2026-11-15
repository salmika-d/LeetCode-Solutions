class Solution(object):
    def isPalindrome(self, s):
       s1=""
       for i in s.lower():
            if i.isalnum():
               s1=s1+i
       if s1[::-1]==s1:
            return True
       else:
            return False