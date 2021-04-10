class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m,n = len(grid),len(grid[0])
        gvisit = set()
        def dfs(i,j,p,ch,lvist):
            if (i,j) in lvist:
                return True
            gvisit.add((i,j))
            lvist.add((i,j))
            for x,y in [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]:
                if 0<=x<m and 0<=y<n and grid[x][y]==ch:
                    if not p or (x,y) != p:
                        if dfs(x,y,(i,j),grid[x][y],lvisit):
                            return True
            return False
        for i in range(m):
            for j in range(n):
                if (i,j) not in gvisit:
                    lvisit = set()
                    if dfs(i,j,None,grid[i][j],lvisit): return True
                    # print(grid)
        return False
        