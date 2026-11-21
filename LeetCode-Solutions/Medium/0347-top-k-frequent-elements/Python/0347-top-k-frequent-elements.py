class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        count=Counter(nums)
        count=count.most_common()
        sol=[]
        for i in range(k):
            sol.append(count[i][0])
        return sol