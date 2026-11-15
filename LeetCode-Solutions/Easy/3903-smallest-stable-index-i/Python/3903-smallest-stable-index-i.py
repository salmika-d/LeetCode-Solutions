class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=len(nums)
        if (l==1):
            return 0
        for i in range(l):
            a = max(nums[0:i+1])
            b = min(nums[i:l])
            if ((a-b)<=k):
                return i
        return -1