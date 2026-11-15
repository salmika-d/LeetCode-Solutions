from collections import Counter
class Solution(object):
    def containsDuplicate(self, nums):
       count=Counter(nums)
       for i in count:
            if count[i]>1:
                return True
       return False
        