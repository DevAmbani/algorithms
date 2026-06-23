# Last updated: 6/23/2026, 6:17:20 PM
1from collections import deque
2
3# Definition for a binary tree node.
4# class TreeNode:
5#     def __init__(self, val=0, left=None, right=None):
6#         self.val = val
7#         self.left = left
8#         self.right = right
9class Solution:
10    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
11        if not root:
12            return []
13        
14        res = []
15        queue = collections.deque()
16        queue.append(root)
17
18        while queue:
19            length = len(queue)
20            level = []
21
22            for q in range(length):
23                node = queue.popleft()
24                level.append(node.val)
25
26                if node.left:
27                    queue.append(node.left)
28                if node.right:
29                    queue.append(node.right)
30            
31            if level:
32                res.append(level)
33        
34        return res
35
36        