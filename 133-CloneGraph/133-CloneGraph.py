# Last updated: 7/14/2026, 5:16:12 PM
1class Solution:
2    def climbStairs(self, n: int) -> int:
3        if n <= 2:
4            return n
5        
6        dp = [0] * (n+1)
7        dp[1] = 1
8        dp[2] = 2
9
10        for i in range(3, n+1):
11            dp[i] = dp[i-1] + dp[i-2]
12        
13        return dp[n]
14