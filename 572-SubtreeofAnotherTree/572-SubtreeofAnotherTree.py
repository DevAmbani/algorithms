# Last updated: 6/13/2026, 2:47:44 PM
1# Definition for a binary tree node.
2class TreeNode:
3    def __init__(self, val=0, left=None, right=None):
4        self.val = val
5        self.left = left
6        self.right = right
7
8class Solution:
9    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
10
11        if (not root) and (not subRoot):
12            return True
13        
14        if (not subRoot):
15            return True
16        
17        if (not root):
18            return False
19        
20        if root.val == subRoot.val:
21            if self.checkTree(root, subRoot):
22                return True
23
24        left = self.isSubtree(root.left, subRoot)
25        right = self.isSubtree(root.right, subRoot)
26
27        return left or right
28        
29    
30    def checkTree(self, root, subRoot):
31        if (not root) and (not subRoot):
32            return True
33        
34        if (not root) or (not subRoot):
35            return False
36        
37        if root.val != subRoot.val:
38            return False
39        
40        left = self.checkTree(root.left, subRoot.left)
41        right = self.checkTree(root.right, subRoot.right)
42
43        return left and right
44