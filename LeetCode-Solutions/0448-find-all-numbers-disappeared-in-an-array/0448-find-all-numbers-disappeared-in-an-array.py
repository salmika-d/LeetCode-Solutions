class Solution(object):
    def findDisappearedNumbers(self, nums):
        num=set(range(1,len(nums)+1))
        return list(num-set(nums))