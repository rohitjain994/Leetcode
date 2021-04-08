class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hasmap = collections.defaultdict(int)
        psum = 0
        mmax = 0
        for i in range(len(nums)):
            psum +=nums[i] if nums[i] else -1
            if psum ==0:
                mmax = max(mmax,i+1) 
            if psum in hasmap:
                mmax = max(mmax,i-hasmap[psum])
            else:
                hasmap[psum] = i
        return mmax
            
            
        