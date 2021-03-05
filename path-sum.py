# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root:
            targetSum = targetSum - root.val
            if not root.left and not root.right and targetSum == 0:
                return True
            return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
        return False
                
        
        
