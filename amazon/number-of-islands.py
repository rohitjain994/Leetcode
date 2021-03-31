class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid),len(grid[0])
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return
            grid[i][j]='0'
            for a,b in [(1,0),(0,-1),(-1,0),(0,1)]:
                dfs(i+a,j+b)
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    dfs(i,j)
                    count+=1
        return count
    #     self.m = len(grid)
    #     self.n = len(grid[0])
    #     self.g = grid
    #     # print(self.g)
    #     self.r = [ -1,  0, 0, 1] 
    #     self.c = [  0, -1, 1, 0]
    #     self.visited = [[False]*self.n for i in range(self.m)]
    #     res = 0
    #     for i in range(self.m):
    #         for j in range(self.n):
    #             # print(i,j,self.visited[i][j],self.g[i][j])
    #             if self.visited[i][j]==False and self.g[i][j]=='1':
    #                 # print(i,j,self.visited[i][j],self.g[i][j])
    #                 self.dfs(i,j)
    #                 res+=1
    #     return res
    # def issafe(self,i,j):
    #     if 0<=i<self.m and 0<=j<self.n and self.visited[i][j]==False and self.g[i][j]=='1':
    #         return True
    #     return False
    # def dfs(self,i,j):
    #     self.visited[i][j] = True
    #     for k in range(4):
    #         if self.issafe(i+self.r[k],j+self.c[k]):
    #             self.dfs(i+self.r[k],j+self.c[k])
        
        