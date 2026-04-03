# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 or not l2:
            return l1 or l2
        curr1 = l1
        curr2 = l2
        cr = False
        prev = None
        node = head = ListNode()
        while curr1 and curr2: 
            s = curr1.val + curr2.val
            if cr:
                s+=1
            if s<10:
                head.val = s
                cr = False 
            else:
                head.val = s-10
                cr = True
            head.next = ListNode()
            prev = head
            head = head.next
            curr1 = curr1.next
            curr2 = curr2.next
        leftover = curr1 or curr2

        while leftover:
            s = leftover.val
            if cr:
                s+=1
            if s<10:
                head.val = s
                cr = False
            else:
                head.val = s-10
            head.next = ListNode()
            prev = head
            head = head.next
            leftover = leftover.next
        if cr:
            head.val = 1
        else:
            prev.next = None
        return node

                
            

#99999
#  11
#  1010                

