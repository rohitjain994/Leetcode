# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
         # 2-pointer streatgy
        h1 = headA
        h2 = headB
        while h1!= h2:
            h1 = h1.next if h1 else headB
            h2 = h2.next if h2 else headA
        return h1
        #Lenghth streatgy
        # l1=self.Listlen(headA)
        # l2 = self.Listlen(headB)
        # l = abs(l1-l2)
        # h1 = headA
        # h2 = headB
        # if l1>l2:
        #     for i in range(0,l):
        #         h1 = h1.next
        # else:
        #     for i in range(0,l):
        #         h2 = h2.next
        # # print(l1,l2,l)
        # while h1 != h2:
        #     h1 = h1.next
        #     h2 = h2.next
        # return h1
       
        
    # def Listlen(self,headA: ListNode) -> int:
    #     h1 = headA
    #     l1 = 0
    #     while h1:
    #         l1+=1
    #         h1 = h1.next
    #     return l1