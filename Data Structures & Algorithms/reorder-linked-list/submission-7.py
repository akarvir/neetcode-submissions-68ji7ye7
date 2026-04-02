# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # probably build it from the middle out 
        n = 0
        curr = head
        while curr:
            n+=1
            curr = curr.next
        curr = head
        for i in range(n//2-1):
            curr = curr.next
        second = curr.next
        curr.next = None

        def reverselist(node):
            if not node or not node.next:
                return node
            prev = None
            curr = node
            after = node.next
            while curr:
                after = curr.next
                curr.next = prev
                prev = curr
                curr = after
            return prev
        
        def mergelist(node1,node2):
            node = head = ListNode()
            curr1 = node1
            curr2 = node2
            f = True
            while curr1 and curr2:
                if f:
                    head.next = curr1
                    curr1 = curr1.next
                else:
                    head.next = curr2
                    curr2 = curr2.next
                f = not f
                head = head.next
            head.next = curr1 or curr2
            return node.next


        mergelist(head,reverselist(second))

        # [0,1,2,3,4,5,6]
        # [0,1,2]
        # [6,5,4,3]
        # [0,6,1,5,2,4,3]
        # it's not a sorted merge. it's literally a merge. 