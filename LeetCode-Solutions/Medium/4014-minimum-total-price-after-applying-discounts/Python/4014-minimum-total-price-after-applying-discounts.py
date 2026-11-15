class Solution(object):
    def minPrice(self, prices, discounts):
        """
        :type prices: List[int]
        :type discounts: List[int]
        :rtype: float
        """
        
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        
        j=0
        bill=0.0
        
        while (j<len(prices) and j<len(discounts)):
            bill+=prices[j]*((100.0-discounts[j])/100.0)
            j+=1
            
        while(j<len(prices)):
            bill+=prices[j]
            j+=1
            
        return bill