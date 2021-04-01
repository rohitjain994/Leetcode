class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        sub = []
        self.allsubset(nums,0,sub,res)
        return res
    def allsubset(self,nums,idx,subset,res):  
            # print(subset)
            res.add(tuple(sorted(subset[:])))
            for i in range(idx,len(nums)):
                subset.append(nums[i])
                self.allsubset(nums,i+1,subset,res)
                subset.pop(-1)
            return
        
# Backtracking + DFS