class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        minv=prices[0]
        p=0
        for i in prices:
            if i <minv:
                minv=i
            elif i-minv > p:
                p=i-minv
        return p
            