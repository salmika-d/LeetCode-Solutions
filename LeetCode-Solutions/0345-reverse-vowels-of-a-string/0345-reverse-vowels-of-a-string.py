class Solution(object):
    def reverseVowels(self, s):
        lv=['a','e','i','o','u','A','E','I','O','U']
        li=[]
        for i in range(len(s)):
            if s[i] in lv:
                li.append(i)
        j=len(li)-1
        s=list(s)
        for i in range(len(li)/2):
            temp=s[li[i]]
            s[li[i]]=s[li[j]]
            s[li[j]]=temp      
            j-=1
        s="".join(s)
        return s