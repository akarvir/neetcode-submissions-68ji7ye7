# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f = head
        s = head
        prev = None
        if not head or not head.next:
            return None
        for i in range(n):
            f = f.next
        while f:
            f = f.next
            prev = s
            s = s.next
        if not prev:
            head = head.next
        else:
            prev.next = prev.next.next
        return head
