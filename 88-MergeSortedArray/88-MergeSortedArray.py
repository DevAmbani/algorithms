# Last updated: 1/30/2026, 10:43:14 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        for i in range(n):
7            nums1[m+i] = nums2[i]
8        nums1.sort()