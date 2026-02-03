# Last updated: 2/3/2026, 9:33:32 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        seen = set()
4        for i in nums:
5            if i in seen:
6                return i
7            seen.add(i)