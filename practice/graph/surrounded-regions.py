class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r = [ -1,  0, 0, 1] 
        c = [  0, -1, 1, 0]
        m = len(board)
        n = len(board[0])
        def dfs(i,j):
            if 0<=i<m and 0<=j<n and board[i][j]=='O':
                board[i][j]='.'
                for k in range(4):
                    dfs(i+r[k],j+c[k])
        for i in range(m):
            if board[i][0] == 'O':dfs(i,0)
            if board[i][n-1] == 'O':dfs(i,n-1)
        for j in range(n):
            if board[0][j]=='O':dfs(0,j)
            if board[m-1][j]=='O':dfs(m-1,j)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='.':
                    board[i][j]='O'
        return board
        