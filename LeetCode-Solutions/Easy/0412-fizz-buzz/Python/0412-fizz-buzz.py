class Solution(object):
    def fizzBuzz(self, n):
        lists=[]
        lists.append(str(1))
        for i in range(1,n):
            if (i+1)%3==0 and (i+1)%5==0:
                lists.append("FizzBuzz")
            elif (i+1)%3==0:
                lists.append("Fizz")
            elif (i+1)%5==0:
                lists.append("Buzz")
            else:
                lists.append(str(i+1))
        return lists 