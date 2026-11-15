class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        l=[]
        res=[]
        for i in strs:
            l.append(sorted(i))
        for i in range(len(strs)):
            res1=[]
            if l[i] != None:
                res1.append(strs[i])
                for j in range(i+1,len(strs)):
                    if l[i] == l[j]:
                        res1.append(strs[j])
                        l[j]=None
                res.append(res1)
                l[i]=None
        return res