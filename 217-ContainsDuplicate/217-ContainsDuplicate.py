# Last updated: 5/13/2026, 11:07:52 PM
1class Solution:
2    def containsDuplicate(self, nums: List[int]) -> bool:
3        seen = set()
4        for n in nums:
5            if n in seen:
6                return True
7            seen.add(n)
8        return False
9        