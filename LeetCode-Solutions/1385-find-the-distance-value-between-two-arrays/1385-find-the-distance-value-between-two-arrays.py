class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        c=0
        for i in arr1:
            f=1
            for j in arr2:
                if abs(i-j) <= d:
                    f=0
                    break
            if f==1:
               c+=1
        return c