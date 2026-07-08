# Last updated: 7/8/2026, 5:22:04 PM
1class Solution:
2    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
3        ans = []
4        state = []
5        candidates.sort()
6
7        def backtrack(start, state, total):
8            if (total == target) and (state not in ans):
9                ans.append(state[:])
10                return
11            
12            if total > target:
13                return
14            
15            for i in range(start, len(candidates)):
16                if i != start and candidates[i] == candidates[i-1]:
17                    continue
18                state.append(candidates[i])
19                backtrack(i+1, state, total + candidates[i])
20                state.pop()
21        
22        backtrack(0, [], 0)
23        return ans
24        