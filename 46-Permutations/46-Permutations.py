# Last updated: 7/8/2026, 3:47:56 PM
1class Solution:
2    def permute(self, nums: List[int]) -> List[List[int]]:
3        ans = []
4        current = []
5
6        def backtrack(state):
7            if (state not in ans) and (len(state) == len(nums)):
8                ans.append(state[:])
9                return
10            
11            for i in range(len(nums)):
12                if nums[i] in state:
13                    continue 
14                state.append(nums[i])
15                backtrack(state)
16                state.pop()
17
18        backtrack([])
19        return ans