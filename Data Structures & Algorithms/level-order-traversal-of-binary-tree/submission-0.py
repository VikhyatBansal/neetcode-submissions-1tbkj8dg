# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        q = deque()
        q.append(root)
        while q:
            sub = []
            for i in range(len(q)):
                curr = q.popleft()
                # print(curr.val)
                if curr.left:
                    q.append(curr.left)
                    # print(curr.left.val)
                if curr.right:
                    q.append(curr.right)
                    # print(curr.right.val)
                sub.append(curr.val)
            res.append(sub)
            # print('----')
        return res

