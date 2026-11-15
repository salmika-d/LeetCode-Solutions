class Solution(object):
    def searchInsert(self, nums, target):
        if(nums.count(target)==0):
            if(target>nums[len(nums)-1]):
                return len(nums)
            for i in range(len(nums)):
               if(target<nums[i]):
                  return i
        for i in range(len(nums)):
            if(target==nums[i]):
                return i



        