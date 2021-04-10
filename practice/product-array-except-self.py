class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [nums[0]]
        for i in range(1,len(nums)):
            res.append(nums[i]*res[i-1])
        # print(res)
        pr = nums[n-1]
        #edge case
        res[n-1] = res[n-2]
        for i in range(n-2,0,-1):
            res[i] = res[i-1]*pr
            pr *= nums[i]
        res[0] = pr
        return res
    
#O(n) O(n)
# without division
# left right multiplication like trapping rain water