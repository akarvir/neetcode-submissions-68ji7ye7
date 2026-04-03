# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        def sametree(p,q):
            if not p or not q:
                temp = p or q
                return not bool(temp )
            return (p.val == q.val) and sametree(p.left,q.left) and sametree(p.right,q.right)
        return sametree(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        