# Last updated: 7/7/2026, 7:16:49 PM
1class Solution:
2    def subsets(self, nums: List[int]) -> List[List[int]]:
3        result = []
4
5        def backtrack(state, start):
6            result.append(state[:])
7            
8            for i in range(start, len(nums)):
9                state.append(nums[i])
10                backtrack(state, i+1)
11                state.pop()
12        
13        backtrack([], 0)
14
15        return result