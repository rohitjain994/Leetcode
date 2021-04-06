# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #l := lower bound r: upper bound
    def isValidBST(self, root: TreeNode,l:TreeNode=None,r:TreeNode=None) -> bool:
        if root == None:
            return True
        if l and root.val <= l.val:
            return False
        if r and root.val >= r.val:
            return False
        return self.isValidBST(root.left,l,root) and self.isValidBST(root.right,root,r)
        