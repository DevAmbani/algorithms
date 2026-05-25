# Last updated: 5/24/2026, 7:01:06 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3
4        for i, n in enumerate(nums):
5            if n == target:
6                return i
7        
8        return -1
9        