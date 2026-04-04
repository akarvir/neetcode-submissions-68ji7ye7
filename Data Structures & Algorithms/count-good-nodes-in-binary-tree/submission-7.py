# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def goodornot(r,p):
            if not r:
                return 0
            c = 1 if r.val >= p else 0
            s  = r.val if r.val>=p else p
            return c + goodornot(r.left,s) + goodornot(r.right,s)
        return goodornot(root,root.val)