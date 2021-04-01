class Solution:
    def findIntersection(self, head1, head2):
        # code here
        # return head of intersection list
        h1 = head1
        h2 = head2
        inter = set()
        res = None
        while h2:
            inter.add(h2.data)
            h2= h2.next
        while h1:
            if h1.data in inter:
                temp = Node(h1.data)
                temp.next = res
                res = temp
            h1 = h1.next
        return res