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

#to get range

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> List[(int,int)]:
        count,rsum = 0,0
        mapsum = collections.defaultdict(list)
        mapsum[0].append(1)
        res = []
        for i in range(len(nums)):
            rsum+=nums[i]
            if rsum == k:
                res.append((0,i))
            if rsum-k in mapsum:
                for it in mapsum[rsum-k]:
                    res.append((it+1,i))
            mapsum[rsum].append(i)
        return res