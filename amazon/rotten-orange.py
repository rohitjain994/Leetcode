class Node:
    def __init__(self,x:int,y:int,t:int)->None:
        self.x = x
        self.y = y
        self.t = t
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append(Node(i,j,0))
        t = 0
        while len(queue)>0:
            temp = queue.pop(0)
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0<=temp.x+i<m and 0<=temp.y+j<n and grid[temp.x+i][temp.y+j]==1:
                    grid[temp.x+i][temp.y+j]=2
                    queue.append(Node(temp.x+i,temp.y+j,temp.t+1))
                    t = temp.t+1
        f = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    f = 1
        return -1 if f else t