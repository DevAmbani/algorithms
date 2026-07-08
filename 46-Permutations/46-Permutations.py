# Last updated: 7/8/2026, 6:42:54 PM
1class Solution:
2    def exist(self, board: List[List[str]], word: str) -> bool:
3        if not word:
4            return True
5
6        q = deque(word)
7        visited = set()
8
9        def dfs(row, col, index):
10            if index == len(word):
11                return True
12            
13            if row < 0 or row >= len(board):
14                return False
15            if col < 0 or col >= len(board[0]):
16                return False
17            
18            if (row, col) in visited:
19                return False
20
21            if word[index] != board[row][col]:
22                return False
23            
24            visited.add((row, col))
25            
26            found = dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1)
27
28            visited.remove((row, col))
29
30            return found
31
32        for row in range(len(board)):
33            for col in range(len(board[0])):
34                if board[row][col] == word[0]:
35                    if dfs(row, col, 0):
36                        return True
37        
38        return False
39              