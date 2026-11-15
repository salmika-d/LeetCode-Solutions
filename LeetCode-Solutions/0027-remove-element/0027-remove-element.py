class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            for j in range(i, len(nums) - 1):
                if nums[i] > nums[j + 1]:
                    temp = nums[i]
                    nums[i] = nums[j + 1]
                    nums[j + 1] = temp     
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[i] != val:
                k = k + 1
                i = i + 1
            else:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                j = j - 1      
        for i in range(k, len(nums)):
            nums[i] = '_'   
        return k