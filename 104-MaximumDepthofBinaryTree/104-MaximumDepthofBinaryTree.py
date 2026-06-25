# Last updated: 6/25/2026, 3:44:40 PM
1from collections import deque
2
3class Solution:
4    def orangesRotting(self, grid: List[List[int]]) -> int:
5        rows = len(grid)
6        cols = len(grid[0])
7        queue = deque()
8        fresh = 0
9        
10        for row in range(rows):
11            for col in range(cols):
12                if grid[row][col] == 2:
13                    queue.append([row, col])
14                if grid[row][col] == 1:
15                    fresh += 1
16        
17        coord = [[0,1], [0,-1], [1,0], [-1,0]]
18        minutes = 0
19                
20        while queue and fresh > 0:
21            minutes += 1
22
23            for _ in range(len(queue)):
24                r, c = queue.popleft()
25
26                for dr, dc in coord:
27
28                    nr, nc = r+dr, c+dc
29                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
30                        grid[nr][nc] = 2
31                        fresh -= 1
32                        queue.append([nr, nc])
33        
34        if fresh == 0:
35            return minutes
36        return -1
37                