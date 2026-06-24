# Last updated: 6/24/2026, 8:54:45 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        values = []
10
11        def order(node):
12            if not node:
13                return None
14            order(node.left)
15            values.append(node.val)
16            order(node.right)
17        
18        order(root)
19        print(values)
20
21        return values[k-1]