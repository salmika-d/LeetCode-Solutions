class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        count=0
        i=0
        while(i<len(nums)):
            d=nums[i]
            for j in range(i,len(nums)):
                if nums[j]==nums[i]:
                    count+=1
                else:
                    break
                if count>len(nums)/2:
                    return nums[i]
            i+=count
        