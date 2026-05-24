# Last updated: 5/23/2026, 11:29:31 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        ans = nums[0]
4        l = 0
5        r = len(nums)-1
6
7        while l < r:
8            mid = (l+r) // 2
9            if nums[mid] > nums[r]:
10                l = mid+1
11            elif nums[mid] < nums[r]:
12                r = mid
13        
14        return nums[l]
15        