# Last updated: 6/24/2026, 8:28:20 AM
1from collections import deque
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def isValidBST(self, root: Optional[TreeNode]) -> bool:
10        if not root:
11            return True
12        
13        values = []
14        def order(node):   
15            if node.left:
16                order(node.left)
17            values.append(node.val)
18            if node.right:
19                order(node.right)
20        
21        order(root)
22        print(values)
23        for i in range(len(values)-1):
24            if (values[i] >= values[i+1]):
25                return False
26        
27        return True