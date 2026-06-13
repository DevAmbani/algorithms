# Last updated: 6/13/2026, 12:53:55 AM
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
12        left = self.maxDepth(root.left)
13        right = self.maxDepth(root.right)
14        
15        return 1 + max(left, right)