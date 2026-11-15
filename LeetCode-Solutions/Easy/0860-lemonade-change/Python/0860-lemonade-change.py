class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        amount=[0]*2
        for i in bills:
            if i == 5:
                amount[0] = amount[0] + 1
            elif i == 10 :
                if amount[0] >= 1:
                    amount[0] = amount[0] - 1
                    amount[1] = amount[1] + 1
                else:
                    return False
            elif i == 20 and amount[1] >= 1 and amount[0] >= 1 :
                amount[1] = amount[1] - 1
                amount[0] = amount[0] - 1 
            elif i == 20 and amount[0] >= 3:
                amount[0] = amount[0] - 3
            else:
                return False
        return True