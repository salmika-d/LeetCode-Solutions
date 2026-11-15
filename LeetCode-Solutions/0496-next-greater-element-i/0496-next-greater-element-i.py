class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res=[]
        f=0
        for i in nums1:
            for j in range(len(nums2)):
                if i==nums2[j]:
                  for k in range(j+1,len(nums2)):
                    if nums2[j]<nums2[k]:
                        res.append(nums2[k])
                        f=1
                        break
                  if f==0:
                    res.append(-1)
                  f=0
                  break 
        return res     