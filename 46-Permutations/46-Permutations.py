# Last updated: 7/10/2026, 10:28:33 AM
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
17            if (row, col) in visited:
18                return False
19
20            if word[index] != board[row][col]:
21                return False
22            
23            visited.add((row, col))
24            
25            found = dfs(row+1, col, index+1) or dfs(row-1, col, index+1) or dfs(row, col+1, index+1) or dfs(row, col-1, index+1)
26
27            visited.remove((row, col))
28
29            return found
30
31        for row in range(len(board)):
32            for col in range(len(board[0])):
33                if board[row][col] == word[0]:
34                    if dfs(row, col, 0):
35                        return True
36        
37        return False
38              