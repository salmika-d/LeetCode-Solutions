class Solution(object):
    def rotateString(self, s, goal):
        if s==goal:
            return True
        elif len(s)==len(goal):
            for i in range(len(s)-1):
                sub1=s[i+1:len(s)]
                sub2=s[0:i+1]
                sub3=sub1+sub2
                if sub3==goal:
                    return True
            return False
        else:
            return False