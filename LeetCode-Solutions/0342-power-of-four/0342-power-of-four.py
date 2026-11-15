class Solution(object):
    def isPowerOfFour(self, n):
        if n in [1,4]:
            return True
        elif n%4==0 and n>1 and n%10 in [1,6,4,5,0]:
            while(n%4==0):
                n=n//4
            if n==1:
                return True
            else:
                return False
        else:
            return False