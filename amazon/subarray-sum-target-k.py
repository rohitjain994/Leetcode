class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count,rsum = 0,0
        mapsum = collections.defaultdict(int)
        mapsum[0] = 1
        for i in range(len(nums)):
            rsum+=nums[i]
            if rsum-k in mapsum:
                count += mapsum[rsum-k]
            mapsum[rsum]+=1
        return count

# Complexity O(n),O(n)
# Prefix sum approach O(n^2)