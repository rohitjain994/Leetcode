# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root == None:
            return -1
        self.min1 = root.val
        self.min2 = float('inf')
        self.getmin(root)
        if self.min2 == float('inf'):
            return -1
        return self.min2
    
    def getmin(self,root):
        if root == None:
            return 
        if root.left and self.min2 > root.left.val > self.min1:
            self.min2 = root.left.val
        if root.right and self.min2 > root.right.val > self.min1:
            self.min2 = root.right.val
        self.getmin(root.left)
        self.getmin(root.right)
        
        
        
