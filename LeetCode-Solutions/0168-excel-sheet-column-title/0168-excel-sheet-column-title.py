class Solution(object):
    def convertToTitle(self, columnNumber):
          var=""
          while(columnNumber>0):
            c1=65
            columnNumber-=1
            temp=columnNumber%26
            i=0
            while (i!=temp):
                 c1+=1
                 i+=1
            columnNumber=columnNumber//26
            var=chr(c1)+var
          return var