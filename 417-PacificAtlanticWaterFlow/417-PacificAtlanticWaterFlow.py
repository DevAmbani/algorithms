# Last updated: 6/28/2026, 2:37:33 PM
1class Solution:
2    def minCostConnectPoints(self, points: List[List[int]]) -> int:
3        n = len(points)
4        parent = list(range(n))
5        rank = [0] * n
6
7        def find(node):
8            if node == parent[node]:
9                return node
10            if node != parent[node]:
11                return find(parent[node])
12        
13        def union(x,y):
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
30        cost = []
31        for i in range(n):
32            for j in range(i+1, n):
33                price = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
34                cost.append([price, i, j])
35        
36        cost.sort()
37        ans = 0
38
39        for price, i, j in cost:
40            if union(i, j):
41                ans += price
42        
43        return ans