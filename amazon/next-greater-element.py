#single list
def nextGreator(arr: List[int]) -> List[int]:
    stack = [arr[0]]
    res = []
    for i in range(1,len(arr)):
        if len(stack)==0:
            stack.append(arr[i])
            continue
        while len(stack)>0 and stack[-1]<arr[i]:
            res.append(arr[i])
            stack.pop()
        stack.append(arr[i])
    while len(stack)>0:
        res.append(-1)
        stack.pop()
    return res
#Circular List 
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [-1]*n
        for i in range(2*n-1,-1,-1):
            while len(stack)>0 and nums[stack[-1]]<=nums[i%n]:
                stack.pop()
            res[i%n] = -1 if len(stack)==0 else nums[stack[-1]]
            stack.append(i%n)
        return res