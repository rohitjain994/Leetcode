#Matrix chain multiplications O(n3) , O(n2)

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums.insert(0,1)
        nums.append(1)
        n = len(nums)
        m = [[0]*n for i in range(n)]
        # for i in range(1,n):
        #     m[i][i] = 0
        for L in range(2,n):
            for i in range(1,n-L+1):
                j = i+L-1
                m[i][j]=0
                # print(i,j)
                for k in range(i,j):
                    # print(m[i][k]+m[k+1][j]+nums[i-1]*nums[k]*nums[j])
                    m[i][j] = max(m[i][j],m[i][k]+m[k+1][j]+nums[i-1]*nums[k]*nums[j])
        # print(nums,m)
        return m[1][n-1]
        