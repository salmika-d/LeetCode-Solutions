class Solution(object):
    def addDigits(self, num):
        if num<=9:
            return num
        else:
            sum=num
            while(sum>9):
                num=sum
                sum=0
                while(num>0):
                  sum+=num%10
                  num=num/10
            return sum