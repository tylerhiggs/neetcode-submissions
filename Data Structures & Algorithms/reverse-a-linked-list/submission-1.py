# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_head = head
        if not head:
            return head
        c = head.next
        head.next = None
        while c:
            temp = c.next
            c.next = current_head
            current_head = c
            c = temp
            
        return current_head