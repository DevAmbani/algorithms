# Last updated: 5/23/2026, 10:11:47 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        ans = nums[0]
4
5        for n in nums:
6            ans = min(ans, n)
7
8        return ans
9        