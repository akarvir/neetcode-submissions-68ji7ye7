# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def isvalid(r,range):
            if not r:
                return True
            if not range[0]<r.val<range[1]:
                return False
            return isvalid(r.left,[range[0],r.val]) and isvalid(r.right,[r.val,range[1]])
        return isvalid(root,[float('-inf'),float('inf')])
        