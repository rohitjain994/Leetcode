class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i,num in enumerate(nums):
            if target-num not in res:
                res[num] = i
            else:
                return [res[target-num],i]
        return []
        