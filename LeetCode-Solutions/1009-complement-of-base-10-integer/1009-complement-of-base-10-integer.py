class Solution(object):
    def bitwiseComplement(self, n):
        num=n
        bin_num=""
        if num==0:
           bin_num+="0"
        while num!=0 :
           value=num%2
           bin_num=str(value)+bin_num
           num=num//2
        bin_num=list(bin_num)
        for i in range(len(bin_num)):
           if(bin_num[i]=="0"):
             bin_num[i]="1"
           else:
             bin_num[i]="0"
        result=""
        for i in bin_num:
            result+=str(i) 
        sum=0
        i=0
        for j in range(len(result)-1,-1,-1):
            sum+=(int(result[j])*math.pow(2,i))
            i=i+1
        return int(sum)
        