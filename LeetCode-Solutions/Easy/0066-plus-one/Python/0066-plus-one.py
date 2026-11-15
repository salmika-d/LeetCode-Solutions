class Solution(object):
    def plusOne(self, digits):
        digits[len(digits)-1]+=1
        for i in range(len(digits)-1,0,-1):
           if(digits[i]>9):
             rem=digits[i]%10
             div=digits[i]//10
             digits[i]=rem 
             digits[i-1]+=div 
        if(digits[0]>9):
            rem = digits[0] % 10
            div = digits[0] // 10
            digits[0] = rem
            digits.insert(0,div)
        return digits 
        