# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def add(root, s):
            if not root:
                return False
            
            s += root.val
            
            if not root.left and not root.right:
                return s == targetSum
            
            return add(root.left, s) or add(root.right, s)
        
        return add(root, 0)

