class Solution(object):
    def strStr(self, haystack, needle):
        n=0
        while(n!=len(haystack)):
         if (needle in haystack):
            for i in range(n,len(haystack)):
                if needle[0]==haystack[i]:
                    index=i
                    break
            c=index
            count=0
            for i in needle:
                if i==haystack[c]:
                    count=count+1
                    c=c+1
            if count==len(needle):
                   return index
            else:
                n=n+1
         else :
            return -1
        