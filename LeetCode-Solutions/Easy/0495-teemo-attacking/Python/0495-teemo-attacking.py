class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        res=0
        c=0
        for i in timeSeries:
            if i<c:
               res+=i+duration-c
            else:
                res+=duration
            c=i+duration
        return res