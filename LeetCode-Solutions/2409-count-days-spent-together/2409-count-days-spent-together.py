class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):

        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        alicea=int(arriveAlice[:2]+arriveAlice[3:])
        alicel=int(leaveAlice[:2]+leaveAlice[3:])
        boba=int(arriveBob[:2]+arriveBob[3:])
        bobl=int(leaveBob[:2]+leaveBob[3:])

        count=0
        month = 1
        for n in range(len(days)):
           for day in range(1, days [n]+1):
               this = (n+1)*100+ day
               if alicea <= this <= alicel and boba <= this <= bobl:
                    count+=1
        return count