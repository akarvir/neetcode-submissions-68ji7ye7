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
        def count(node,m):
            counter = 0
            if not node:
                return counter
            if node.val >=m:
                counter+=1
            p = max(node.val,m)
            return counter + count(node.left,p) + count(node.right,p)
        return count(root,root.val)