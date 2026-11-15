class Solution(object):
    def minOperations(self, s):
        count = 0
        change = 0
        s_list = list(s)
        
        for i in range(len(s_list) - 1):
            if s_list[i] == '0' and s_list[i+1] == '0':     
                s_list[i+1] = '1' 
                change += 1   
            elif s_list[i] == '1' and s_list[i+1] == '1':
                s_list[i+1] = '0'
                change += 1

        s_list2 = list(s)
        s_list2[0] = '1' if s[0] == '0' else '0'
        change2 = 1 
        
        for i in range(len(s_list2) - 1):
            if s_list2[i] == '0' and s_list2[i+1] == '0':     
                s_list2[i+1] = '1' 
                change2 += 1   
            elif s_list2[i] == '1' and s_list2[i+1] == '1':
                s_list2[i+1] = '0'
                change2 += 1

        return min(change, change2)
