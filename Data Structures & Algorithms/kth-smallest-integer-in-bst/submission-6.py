# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []
        def dfs(r):
            nonlocal l
            if not r:
                return 0
            dfs(r.left)
            l.append(r.val)
            dfs(r.right)
        dfs(root)
        return l[k-1]
                
        