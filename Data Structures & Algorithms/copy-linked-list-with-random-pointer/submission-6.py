"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        d = {}
        curr = head
        while curr:
            a = Node(curr.val)
            d[curr] = a
            curr = curr.next
        for k in d:
            next = k.next
            r = k.random
            if next in d: 
                d[k].next = d[next]
            if r in d:
                d[k].random = d[r]
        return d[head]
        