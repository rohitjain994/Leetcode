class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Swapping balls
        j = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i],nums[j] = nums[j],nums[i]
                j+=1
        k = len(nums)-1
        for i in range(len(nums)-1,j-1,-1):
            if nums[i] == 2:
                nums[i],nums[k] = nums[k],nums[i]
                k-=1
        # dic = collections.defaultdict(int)
        # for i in nums:
        #     dic[i]+=1
        # p = 0
        # i = 0
        # while i < len(nums):
        #     if dic[p]>0:
        #         nums[i] = p
        #         i+=1
        #         dic[p]-=1
        #     else:
        #         p+=1
        # print(dic)
