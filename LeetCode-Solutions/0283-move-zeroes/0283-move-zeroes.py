class Solution(object):
    def moveZeroes(self, nums):
        if nums.count(0)==0 or len(nums)==1 or nums.count(0)==len(nums):
            return nums
        else:
            c=nums.count(0) 
            i=0 
            while(i!=len(nums)):
                if nums[i]==0:
                    nums.remove(0)
                else:
                    i=i+1
            for i in range(c):
                nums.append(0)
            return nums     