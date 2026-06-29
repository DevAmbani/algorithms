# Last updated: 6/29/2026, 10:14:40 AM
1class Solution:
2    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
3        matrix = []
4
5        for rows in range(n):
6            row = []
7            for cols in range(n):
8                if rows == cols:
9                    row.append(0)
10                else:
11                    row.append(float('inf'))
12            matrix.append(row)
13
14        for src, dest, cost in edges:
15            matrix[src][dest] = cost
16            matrix[dest][src] = cost
17        
18        for k in range(n):
19            for i in range(n):
20                for j in range(n):
21                    if matrix[i][k] + matrix[k][j] < matrix[i][j]:
22                        matrix[i][j] = matrix[i][k] + matrix[k][j]
23        
24        ans = -1
25        ans_count = float('inf')
26        for row in range(n):
27            count = 0
28            for col in range(n):
29                if matrix[row][col] <= distanceThreshold:
30                    count += 1
31            
32            if count <= ans_count:
33                ans_count = count
34                ans = row
35        
36        return ans
37
38