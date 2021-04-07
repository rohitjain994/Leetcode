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

https://leetcode.com/problems/next-greater-element-i/
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapper = {e:i for i,e in enumerate(nums2)}
        stack = []
        res = [-1]*len(nums2)
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                res[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(i) 
        return [res[mapper[i]] for i in nums1]

#Next greator number
stack = []
res = [-1]*len(nums)
for i in range(len(nums)): 
    while stack and nums[stack[-1]]<nums[i]:
        res[stack[-1]] = nums[i]
        stack.pop()
    stack.append(i)
#Previous greator number
stack = [nums[0]]
res = [-1]
for i in range(1,len(nums)):
    while stack and stack[-1] < nums[i]:
        stack.pop()
    res.append(stack[-1] if stack else -1)
    stack.append(nums[i])
