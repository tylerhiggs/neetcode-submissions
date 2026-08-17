# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: Optional[int], high: Optional[int]) -> bool:
            if not node:
                return True
            return (low == None or low < node.val) and (high == None or node.val < high) and valid(node.left, low, node.val) and valid(node.right, node.val, high)
        
        return valid(root, None, None)