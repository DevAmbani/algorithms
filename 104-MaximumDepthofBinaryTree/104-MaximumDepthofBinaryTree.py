# Last updated: 6/25/2026, 9:31:31 AM
1class Solution:
2    def numIslands(self, grid: List[List[str]]) -> int:
3        count = 0
4        rows = len(grid)
5        elements = len(grid[0])
6
7        def dfs(row, element):
8            if row >= rows or row < 0:
9                return
10            if element >= elements or element < 0:
11                return
12            if grid[row][element] == '0':
13                return
14            
15            if grid[row][element] == '1':
16                grid[row][element] = '0'
17
18            dfs(row+1, element)
19            dfs(row-1, element)      
20            dfs(row, element+1)
21            dfs(row, element-1)
22
23        for row in range(len(grid)):
24            for element in range(len(grid[0])):
25                if grid[row][element] == '1':
26                    count += 1
27                    dfs(row, element)
28        
29        return count