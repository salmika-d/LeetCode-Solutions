class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if(len(nums2)==0):
            return nums1
        else:
            for i in range(len(nums1)-1,-1,-1):
                if nums1[i]==0:
                    for j in nums2:
                        nums1[i]=j
                        i=i-1
                    return nums1.sort()