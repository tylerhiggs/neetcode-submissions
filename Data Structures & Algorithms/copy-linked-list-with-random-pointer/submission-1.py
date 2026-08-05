"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        # First pass
        if not head:
            return head
        c = head
        c1 = Node(c.val)
        c1.random = c.random
        head1 = c1
        d = {None: None, c: c1}
        while c.next:
            c1.next = Node(c.next.val)
            c1.next.random = c.next.random
            d[c.next] = c1.next
            c1 = c1.next
            c = c.next
        c = head
        while c:
            d[c].random = d[d[c].random]
            c = c.next
        return head1
        
