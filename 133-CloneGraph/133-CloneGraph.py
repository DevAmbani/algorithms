# Last updated: 7/13/2026, 4:35:45 PM
1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, val = 0, neighbors = None):
5        self.val = val
6        self.neighbors = neighbors if neighbors is not None else []
7"""
8
9from typing import Optional
10class Solution:
11    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
12        cloned = {}
13
14        def dfs(node):
15            if node in cloned:
16                return cloned[node]
17            
18            clone = Node(node.val)
19            cloned[node] = clone
20            
21            for neighbor in node.neighbors:
22                soln = dfs(neighbor)
23                clone.neighbors.append(soln)
24            
25            return clone
26        
27        return dfs(node) if node else None
28        