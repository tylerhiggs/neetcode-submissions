"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(current: Optional['Node']) -> Optional['Node']:
            if not current:
                return
            if current in old_to_new:
                return old_to_new[current]
            new_node = Node(current.val)
            old_to_new[current] = new_node
            neighbors = [dfs(neighbor) for neighbor in current.neighbors]
            new_node.neighbors = neighbors
            return new_node
        return dfs(node)

            
            
            
            
