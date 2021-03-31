# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #Without Extra space
        if head:
            if not head.next:
                return True
            sec_half = self.second_half(head)
            sec_half = self.reverse(sec_half)
            # self.printval(sec_half)
            # print()
            # self.printval(head)
            return self.compare(head,sec_half)
        return True
    def reverse(self,head: ListNode) -> ListNode:
        cur = head
        prv = None
        while cur:
            next = cur.next
            cur.next = prv
            prv = cur
            cur = next
        head = prv
        return head
    def second_half(self,head: ListNode):
        cur = p = pp = head
        mid = None
        while cur and cur.next:
            cur = cur.next.next
            pp = p
            p = p.next
        if cur:
            mid = p
            p = p.next
        pp.next = None
        return p
    def compare(self,l1: ListNode,l2: ListNode) -> bool:
        h1 = l1
        h2 = l2
        while(h1 and h2):
            if h1.val!=h2.val:
                return False
            h1 = h1.next
            h2 = h2.next
        if not h1 and not h2:
            return True
        return False
        
    def printval(self,head:ListNode) :
        cur = head
        while cur:
            print(cur.val,end=' ')
            cur = cur.next
    