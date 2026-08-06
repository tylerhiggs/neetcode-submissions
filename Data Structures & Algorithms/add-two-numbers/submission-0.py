# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        c1 = l1
        c2 = l2
        c = ListNode()
        new_head = c
        # 99
        # 99
        while c1 or c2:
            if not c1:
                c.val = (c2.val + carry) % 10
                carry = (c2.val + carry) // 10
                c2 = c2.next
            elif not c2:
                c.val = (c1.val + carry) % 10
                carry = (c1.val + carry) // 10
                c1 = c1.next
            else:
                c.val = (c1.val + c2.val + carry) % 10
                carry = (c1.val + c2.val + carry) // 10
                c1 = c1.next
                c2 = c2.next
            if c1 or c2 or carry:
                c.next = ListNode()
                c = c.next
        if carry:
            c.val = carry
        return new_head

