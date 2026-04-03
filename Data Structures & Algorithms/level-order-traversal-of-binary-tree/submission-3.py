# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        d = deque()
        # have a while loop within there. 
        d.append(root)
        res = []
        while d:
            res.append([])
            l = len(d)
            for i in range(len(d)): 
                node = d.popleft()
                res[-1].append(node.val)
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return res