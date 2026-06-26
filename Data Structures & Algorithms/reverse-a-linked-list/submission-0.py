# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        hp = head
        rp = head.next
        head.next = None
        while rp:
            next_p = rp.next
            rp.next = hp
            hp = rp
            rp = next_p
        return hp