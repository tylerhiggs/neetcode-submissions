# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        def dfs(r: Optional[TreeNode], l: List[List[int]], level=0):
            if not r:
                return
            if len(res) == level:
                res.append([])
            res[level].append(r.val)
            dfs(r.left, l, level + 1)
            dfs(r.right, l, level + 1)
        dfs(root, res)
        return res