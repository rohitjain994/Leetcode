class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = [ -1,  0, 0, 1] 
        c = [  0, -1, 1, 0]
        def dfs(grid,i,j):
            if i<0 or j<0 or i==len(grid) or j==len(grid[i]) or grid[i][j]==0:
                return 0
            grid[i][j]=0
            cnt = 1
            for k in range(4):
                cnt+=dfs(grid,i+r[k],j+c[k])
            return cnt
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==1:
                    res = max(res,dfs(grid,i,j))
        return res
#         self.m = len(grid)
#         self.n = len(grid[0])
#         self.g = grid
#         # print(self.g)
#         self.r = [ -1,  0, 0, 1] 
#         self.c = [  0, -1, 1, 0]
#         self.visited = [[False]*self.n for i in range(self.m)]
#         res = 0
#         for i in range(self.m):
#             for j in range(self.n):
#                 # print(i,j,self.visited[i][j],self.g[i][j])
#                 if self.visited[i][j]==False and self.g[i][j]==1:
#                     # print(i,j,self.visited[i][j],self.g[i][j])
#                     res = max(res,self.dfs(i,j))
                    
#         return res
#     def issafe(self,i,j):
#         if 0<=i<self.m and 0<=j<self.n and self.visited[i][j]==False and self.g[i][j]==1:
#             return True
#         return False
#     def dfs(self,i,j):
#         self.visited[i][j] = True
#         res = 1
#         for k in range(4):
#             if self.issafe(i+self.r[k],j+self.c[k]):
#                 res+=self.dfs(i+self.r[k],j+self.c[k])
#         return res