class Solution(object):
    def findWords(self, words):

        f = "qwertyuiop"
        s = "asdfghjkl"
        t = "zxcvbnm"

        l=[]
   
        for i in words:
            if i[0].lower() in f:
                ta=f
            elif i[0].lower() in s:
                ta=s
            else:
                ta=t
            for char in i:
                if char.lower() not in ta:
                    break
            if char.lower() in ta and char==i[len(i)-1]:
                l.append(i)
        return l 