# Last updated: 2/12/2026, 9:22:17 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
9        if not subRoot:
10            return True
11
12        if not root:
13            return False
14
15        if self.sameTree(root, subRoot):
16            return True
17        
18        left = self.isSubtree(root.left, subRoot)
19        right = self.isSubtree(root.right, subRoot)
20
21        return left or right
22
23    def sameTree(self, r, sR) -> bool:
24        if not r and not sR:
25            return True
26        
27        if not r or not sR:
28            return False
29        
30        if r.val != sR.val:
31            return False
32
33        left = self.sameTree(r.left,sR.left)
34        right = self.sameTree(r.right,sR.right)
35
36        return left and right