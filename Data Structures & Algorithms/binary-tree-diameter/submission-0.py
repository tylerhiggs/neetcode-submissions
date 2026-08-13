# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def help(r: Optional[TreeNode]) -> [int, int]:
            # maxDepth, bestResult
            if not r:
                return [0, 0]
            right, left = help(r.right), help(r.left)
            return [1 + max(right[0], left[0]), max(right[1], left[1], right[0] + left[0])]
        [max_depth, best_result] = help(root)
        return best_result

