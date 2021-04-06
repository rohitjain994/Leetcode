class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top,down,left,right=0,len(matrix)-1,0,len(matrix[0])-1
        res = []
        while left<=right and top<=down:
            for i in range(left,right+1):
                res.append(matrix[top][i])

            for i in range(top+1,down+1):
                res.append(matrix[i][right])
            if left<right and top<down:
                for i in range(right-1,left,-1):
                    res.append(matrix[down][i])

                for i in range(down,top,-1):
                    res.append(matrix[i][left])
            top+=1
            down -=1
            left+=1
            right-=1
        return res
        