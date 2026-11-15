from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        c2=Counter(nums2)
        result=[]
        for i in nums1:
            if c2[i]>0:
                result.append(i)
                c2[i]-=1
        return result