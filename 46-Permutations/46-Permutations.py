# Last updated: 7/8/2026, 3:48:03 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        ans = []
4        current = []
5
6        def backtrack(state):
7            if (state not in ans) and (len(state) == len(nums)):
8                ans.append(state[:])
9            
10            for i in range(len(nums)):
11                if nums[i] in state:
12                    continue 
13                state.append(nums[i])
14                backtrack(state)
15                state.pop()
16
17        backtrack([])
18        return ans