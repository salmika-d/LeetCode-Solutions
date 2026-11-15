class Solution(object):
    def countServers(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        c=0
        m = len(grid)
        n = len(grid[0])
        temp = [[0] * n for _ in range(m)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    c+=1
            if c>1:
                for j in range(len(grid[0])):
                  if grid[i][j]==1:
                    temp[i][j]=1
            c=0
        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i]==1:
                    c+=1
            if c>1:
                for j in range(len(grid)):
                    if grid[j][i]==1:
                       temp[j][i]=1
            c=0
        return sum(sum(temp, []))