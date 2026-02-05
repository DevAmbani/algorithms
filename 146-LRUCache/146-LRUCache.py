# Last updated: 2/4/2026, 8:57:47 PM
1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0  # index for next valid element
4
5        for i in range(len(nums)):
6            if nums[i] != val:
7                nums[k] = nums[i]
8                k += 1
9
10        return k
11