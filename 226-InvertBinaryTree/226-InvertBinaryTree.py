# Last updated: 2/9/2026, 10:32:03 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        if not root:
10            return None
11        
12        temp = root.left
13        root.left = root.right
14        root.right = temp
15
16        self.invertTree(root.left)
17        self.invertTree(root.right)
18
19        return root