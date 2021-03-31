class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = collections.defaultdict(int)
        for i in nums:
            dic[i]+=1
        p = 0
        i = 0
        while i < len(nums):
            if dic[p]>0:
                nums[i] = p
                i+=1
                dic[p]-=1
            else:
                p+=1
        # print(dic)
