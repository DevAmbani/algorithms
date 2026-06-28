# Last updated: 6/28/2026, 8:47:54 AM
1class Solution:
2    def countComponents(self, n: int, edges: List[List[int]]) -> int:
3        parent = list(range(n))
4        rank = [0] * n
5        components = n
6
7        def find(node):
8            if parent[node] == node:
9                return node
10            elif parent[node] != node:
11                return find(parent[node])
12        
13        def union(x, y):
14            px = find(x)
15            py = find(y)
16
17            if px == py:
18                return False
19
20            if rank[px] > rank[py]:
21                parent[py] = px
22            elif rank[py] > rank[px]:
23                parent[px] = py
24            else:
25                parent[py] = px
26                rank[px] += 1
27
28            return True
29        
30        for x,y in edges:
31            if union(x,y):
32                components -= 1
33        
34        return components