class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            n = []
            for i in range(0, len(s), k):
                c = s[i:i + k]
                total=0
                for i in c:
                    total+=int(i)
                n.append(str(total))
            s = "".join(n)
        return s