# Last updated: 6/25/2026, 5:57:32 PM
1from collections import deque
2
3class Solution:
4    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
5        rows = len(heights)
6        cols = len(heights[0])
7        poq = deque()
8        aoq = deque()
9
10        def bfs(queue):
11            directions = [[1,0],[-1,0],[0,1],[0,-1]]
12            visited = set(queue)
13            while queue:
14                for _ in range(len(queue)):
15                    r, c = queue.popleft()
16                    for dr, dc in directions:
17                        nr, nc = r+dr, c+dc
18                        
19                        if 0 <= nr < rows and 0 <= nc < cols and heights[r][c] <= heights[nr][nc] and (nr,nc) not in visited:
20                            queue.append([nr, nc])
21                            visited.add((nr,nc))
22            return visited
23
24        for row in range(rows):
25            for col in range(cols):
26                if row == 0 or col == 0:
27                    poq.append((row, col))
28                if row == rows-1 or col == cols-1:
29                    aoq.append((row, col))
30        
31        pacific = bfs(poq)
32        atlantic = bfs(aoq)
33        ans = []
34
35        for element in pacific:
36            if element in atlantic:
37                ans.append(element)
38        
39        return ans
40        