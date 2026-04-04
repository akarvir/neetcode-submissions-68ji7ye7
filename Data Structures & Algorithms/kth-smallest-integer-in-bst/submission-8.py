# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s = -1
        count = 0
        def dfs(r):
            nonlocal count
            nonlocal s
            if not r:
                return
            dfs(r.left)
            count+=1
            if count == k:
                s = r.val
                return
            dfs(r.right)
        dfs(root)
        return s
                
        