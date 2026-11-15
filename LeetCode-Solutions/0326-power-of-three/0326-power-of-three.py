class Solution(object):
    def isPowerOfThree(self, n):
        if n<1:
            return False
        else:
            li=[9,7,1,3]
            if n%10 in li :
               if (n%3==0 or n==1) :
                while n%3==0:
                    n=n//3
                if n==1:
                   return True
            return False