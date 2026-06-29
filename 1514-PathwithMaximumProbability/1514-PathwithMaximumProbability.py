# Last updated: 6/29/2026, 1:39:43 PM
1from collections import deque
2
3class Solution:
4    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
5        directions = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,-1],[-1,1]]
6        visited = set()
7        queue = deque()
8        start = [0,0,1]
9        queue.append(start)
10        visited.add((0,0))
11        n = len(grid)-1
12
13        if grid[0][0] == 1 or grid[n][n] == 1:
14            return -1
15
16        while queue:
17            r, c, distance = queue.popleft()
18            if r == n and c == n:
19                return distance
20            for dr, dc in directions:
21                nr , nc = r+dr, c+dc
22                if (0 <= nr <= n) and (0 <= nc <= n) and ((nr,nc) not in visited) and (grid[nr][nc] == 0):
23                    queue.append([nr, nc, distance+1])
24                    visited.add((nr,nc))
25        
26        return -1
27            