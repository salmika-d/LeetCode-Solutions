class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        if len(nums)==0 or nums.count(1)==0:
            return 0
        elif nums.count(1)==1:
            return 1
        else:
          c=0
          max=0
          for i in nums+[0]:
            if i==1:
                c+=1
            else:
                if max<c:
                    max=c
                c=0
          return max