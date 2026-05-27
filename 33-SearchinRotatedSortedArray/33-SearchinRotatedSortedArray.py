# Last updated: 5/27/2026, 6:57:12 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        l = 0
4        ans = 0
5        lowest = prices[0]
6
7        for r in range(len(prices)):
8            lowest = min(lowest, prices[r])
9            compare = prices[r] - lowest
10            ans = max(ans, compare)
11
12        return ans