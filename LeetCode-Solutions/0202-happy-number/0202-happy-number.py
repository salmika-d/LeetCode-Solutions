class Solution(object):
    def isHappy(self, n):
        sum=0
        while(n>4):
            while(n!=0):
                a=n%10
                n=n//10
                sum+=(a*a)
            n=sum
            sum=0
        if(n==1):
            return True
        else:
            return False