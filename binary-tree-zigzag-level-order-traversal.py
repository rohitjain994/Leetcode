# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def level(node):
            if not node:
                return 0
            if not node.left and not node.right:
                return 1
            return 1+max(level(node.left),level(node.right))
        def levelorder(node,lvl):
            if not node:
                return []
            if lvl == 1:
                return [node.val]
            return levelorder(node.left,lvl-1)+levelorder(node.right,lvl-1)
        res = []
        height = level(root)
        for i in range(1,height+1):
            if i&1:
                res.append(levelorder(root,i))
            else:
                res.append(levelorder(root,i)[::-1])
        return res
                
                
        
