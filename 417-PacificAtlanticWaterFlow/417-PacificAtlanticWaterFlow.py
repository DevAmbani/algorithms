# Last updated: 6/28/2026, 11:10:50 AM
1class Solution:
2    def validTree(self, n: int, edges: List[List[int]]) -> bool:
3        rank = [0] * n
4        parent = list(range(n))
5
6        if n-1 != len(edges):
7            return False
8
9        def find(node):
10            if node == parent[node]:
11                return node
12            if node != parent[node]:
13                return find(parent[node])
14        
15        def union(x, y):
16            px = find(x)
17            py = find(y)
18
19            if px == py:
20                return False
21            
22            if rank[px] > rank[py]:
23                parent[py] = px
24            elif rank [py] > rank[px]:
25                parent[px] = py
26            else:
27                parent[py] = px
28                rank[px] += 1
29            
30            return True
31        
32        for x,y in edges:
33             if union(x,y) is False:
34                return False
35        
36        return True