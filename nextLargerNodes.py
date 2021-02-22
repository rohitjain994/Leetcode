# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        res = [0]
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        stack = [arr[-1]]
        for i in range(len(arr)-2,-1,-1):
            # print(arr[i])
            if stack[-1] > arr[i]:
                res.append(stack[-1])
            else:
                while len(stack) > 0 and stack[-1] <= arr[i]:
                    stack.pop()
                if len(stack) == 0:
                    res.append(0)
                else:
                    res.append(stack[-1])
            stack.append(arr[i])
        return res[::-1]
        
        # Brute Force n^2
        # cur = head
        # while cur:
        #     m = cur.val
        #     p = cur.next
        #     while p:
        #         if p.val > m:
        #             m = p.val
        #             break
        #         p = p.next
        #     if m == cur.val:
        #         m = 0
        #     res.append(m)
        #     cur = cur.next
        # return res
        