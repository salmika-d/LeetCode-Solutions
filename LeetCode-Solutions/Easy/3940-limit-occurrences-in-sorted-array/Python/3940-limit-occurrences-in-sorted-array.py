class Solution(object):
    def limitOccurrences(self, nums, k):
        i=0
        while(i<len(nums)):
            n=nums.count(nums[i])
            if(n>k):
                j=n-k
                i+=k
                while(j!=0):
                    nums.remove(nums[i])
                    j-=1
            else:
                i+=n
        return nums
        