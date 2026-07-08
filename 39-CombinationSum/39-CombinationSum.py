# Last updated: 7/7/2026, 7:56:20 PM
1class Solution:
2    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
3        ans = []
4        total = 0
5
6        def backtrack(state, start, total):
7            if total == target:
8                ans.append(state[:])
9                return
10            
11            if total > target:
12                return
13            
14            for i in range(start, len(candidates)):
15                state.append(candidates[i])
16                total = sum(state)
17                backtrack(state, i, total)
18                state.pop()
19        
20        backtrack([], 0, 0)
21        return ans
22    