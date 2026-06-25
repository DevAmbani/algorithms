# Last updated: 6/25/2026, 10:53:46 AM
1class Solution:
2    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
3        rows = len(grid)
4        elements = len(grid[0])
5        maxarea = 0
6
7        def dfs(row, element):
8            if row < 0 or row >= rows:
9                return 0
10            if element < 0 or element >= elements:
11                return 0
12            if grid[row][element] == 0:
13                return 0
14            
15            grid[row][element] = 0
16            
17            return 1 + dfs(row+1, element) + dfs(row-1, element) + dfs(row, element+1) + dfs(row, element-1)
18
19        for row in range(len(grid)):
20            for element in range(len(grid[0])):
21                if grid[row][element] == 1:
22                    area = dfs(row, element)
23                    maxarea = max(maxarea, area)
24        
25        return maxarea
26        