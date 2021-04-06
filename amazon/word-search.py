class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        def bt(r,c,idx):
            if len(word)==idx:
                return True
            if 0<=r<m and 0<=c<n and board[r][c]==word[idx]:
                T = board[r][c]
                board[r][c]=""
                for i,j in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:   
                    if bt(i,j,idx+1): 
                        return True
                board[r][c]=T
            return False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0] and bt(i,j,0): return True
        return False