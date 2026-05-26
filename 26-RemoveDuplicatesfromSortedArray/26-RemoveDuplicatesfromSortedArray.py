# Last updated: 5/25/2026, 10:53:19 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 1  # pointer for the next unique element position
4
5        for i in range(1, len(nums)):
6            if nums[i] != nums[i - 1]:
7                nums[k] = nums[i]
8                k += 1
9
10        return k