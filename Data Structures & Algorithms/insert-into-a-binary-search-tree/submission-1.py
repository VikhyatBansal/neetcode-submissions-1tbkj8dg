# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # print(root.val)
        if not root:
            return TreeNode(val)
        if root.left==None and root.val>val:
            root.left = TreeNode(val)
        elif root.right==None and root.val<val:
            root.right = TreeNode(val)
        elif root.val>val:
            self.insertIntoBST(root.left,val)
        else:
            self.insertIntoBST(root.right,val)           
        
        return root