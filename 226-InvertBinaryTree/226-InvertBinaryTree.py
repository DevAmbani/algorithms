# Last updated: 2/10/2026, 5:18:04 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11
12        left_depth = self.maxDepth(root.left)
13        right_depth = self.maxDepth(root.right)
14
15        return 1 + max(left_depth, right_depth)