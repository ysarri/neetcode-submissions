# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxL = self.maxDepth(root.left)
        maxR = self.maxDepth(root.right)
        print(maxL+1, maxR+1)
        return 1 + max(maxL, maxR)
        