# Last updated: 7/8/2026, 3:55:24 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        ans = []
4
5        def backtrack(state):
6            if (state not in ans) and (len(state) == len(nums)):
7                ans.append(state[:])
8            
9            for i in range(len(nums)):
10                if nums[i] in state:
11                    continue 
12                state.append(nums[i])
13                backtrack(state)
14                state.pop()
15
16        backtrack([])
17        return ans