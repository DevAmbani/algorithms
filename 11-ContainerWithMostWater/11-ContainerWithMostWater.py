# Last updated: 5/22/2026, 11:11:16 AM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        ans = 0
4        l ,r = 0, len(height)-1
5
6        while l < r:
7            area = (r-l) * (min(height[l], height[r]))
8            ans = max(ans, area)
9            if height[l] >= height[r]:
10                r -= 1
11            else:
12                l += 1
13
14        return ans
15