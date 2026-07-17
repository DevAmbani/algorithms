# Last updated: 7/17/2026, 12:45:46 PM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        if len(nums) == 0:
4            return 0
5        if len(nums) == 1:
6            return nums[0]
7        if len(nums) == 2:
8            return max(nums[0], nums[1])
9
10        def dp(nums):
11            dp = [0] * len(nums)
12            dp[0] = nums[0]
13            dp[1] = max(nums[0], nums[1])
14
15            for i in range(2, len(nums)):
16                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
17            
18            return dp[len(nums)-1]
19            
20        return max(dp(nums[1:]),dp(nums[:-1]))