# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        #Result Array 
        res = [0]
        #reverse List
        cur = head
        prv = None
        while cur:
            next = cur.next
            cur.next = prv
            prv = cur
            cur = next
        cur = prv
        #stack
        stack = [cur.val]
        cur = cur.next
        while cur:
            # print(arr[i])
            if stack[-1] > cur.val:
                res.append(stack[-1])
            else:
                while len(stack) > 0 and stack[-1] <= cur.val:
                    stack.pop()
                if len(stack) == 0:
                    res.append(0)
                else:
                    res.append(stack[-1])
            stack.append(cur.val)
            cur = cur.next
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
        