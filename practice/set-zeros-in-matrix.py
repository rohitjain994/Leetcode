class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r,c = len(matrix),len(matrix[0])
        row,col = set(),set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] ==0:
                    row.add(i)
                    col.add(j)
        for i in range(r):
            for j in range(c):
                if i in row or j in col:
                    matrix[i][j] = 0
        
        