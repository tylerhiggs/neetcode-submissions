# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: Optional[TreeNode], val: int) -> int:
            if not node:
                return 0
            if node.val < val:
                new_val = val
                c = 0
            else:
                new_val = node.val
                c = 1
            return dfs(node.left, new_val) + dfs(node.right, new_val) + c
        return dfs(root, root.val)