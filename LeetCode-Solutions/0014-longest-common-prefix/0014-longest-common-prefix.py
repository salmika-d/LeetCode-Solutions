class Solution(object):
    def longestCommonPrefix(self, strs):
        s=""
        count=0
        n=len(strs[0])
        for i in range(len(strs)-1):
            if(n>len(strs[i+1])):
                n=len(strs[i+1])
            if(len(strs[i])==0):
                return s
        if(len(strs)>1):
         for i in range (n):
            for j in range(len(strs)-1):
                if(strs[j][i]==strs[j+1][i]):
                    count=count+1   
                else:
                    break
            if(count==(len(strs)-1)):
                s=s+strs[j][i]
                count=0
            else:
                break
        else:
            s=s+strs[0]
        return s