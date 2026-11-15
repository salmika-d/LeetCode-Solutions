class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        c=len(candyType)/2
        u=len(set(candyType))
        if u>c:
            return c
        else:
            return u