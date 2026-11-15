class Solution(object):
    def weightedSum(self, parent, nums):
        """
        :type parent: List[int]
        :type nums: List[int]
        :rtype: int
        """

        n = len(parent)
        d = [0] * n
        d[0] = 1
        
        def getd(ind):
            if d[ind] != 0:
                return d[ind]
            d[ind] = getd(parent[ind]) + 1
            return d[ind]
            
        for i in range(n):
            getd(i)
            
        h = max(d)
        total = 0
        for i in range(n):
            total += nums[i] * (h - d[i] + 1)
            
        return total