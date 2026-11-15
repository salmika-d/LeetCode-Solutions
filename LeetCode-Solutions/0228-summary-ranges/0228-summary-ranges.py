class Solution(object):
    def summaryRanges(self, nums):
        if len(nums)==0:
            return []
        l=[]
        s=""
        j=0
        for i in range(len(nums)):
            if j==0:
                s=s+str(nums[i])
                j=1
            if i+1==len(nums) or (nums[i+1])!=nums[i]+1:
                if s!=str(nums[i]):
                   s=s+"->"
                   s=s+str(nums[i])              
                l.append(s)
                s=""
                j=0
        return l