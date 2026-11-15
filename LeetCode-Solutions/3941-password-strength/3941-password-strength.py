class Solution(object):
    def passwordStrength(self, password):
        s=0
        s1=""
        for i in password:
            if i not in s1:
                s1=s1+i
        for i in s1:
            if i.isalnum():
                if i>='a' and i<='z':
                    s+=1
                elif i>='A' and i<='Z':
                    s+=2
                elif int(i)>=0 and int(i)<=9:
                    s+=3
            else:
                s+=5
        return s