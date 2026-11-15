class Solution(object):
    def climbStairs(self, n):
        if n<4:
            return n
        c=[1]*n
        count=1
        k=n-1
        for i in range(int(n/2)):
            del c[k]
            c[i]=2
            r=c.count(1)
            r1=c.count(2)
            fr=fr1=num=1
            for i in range(1,len(c)+1):
                num=num*i
            for i in range(1,r+1):
                fr1=fr1*i
            for i in range(1,r1+1):
                fr=fr*i
            count=count+(num/(fr*fr1))
            k=k-1
        return count 