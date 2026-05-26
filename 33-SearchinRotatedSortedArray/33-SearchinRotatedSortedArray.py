# Last updated: 5/26/2026, 12:27:27 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l = 0
4        r = len(nums) - 1
5        
6        while l <= r:
7            mid = (l+r) // 2
8            if nums[mid] == target:
9                return mid
10            elif nums[l] > nums[mid]:
11                if target <= nums[r] and target > nums[mid]:
12                    l = mid+1
13                else:
14                    r = mid-1
15            else:
16                if target >= nums[l] and target < nums[mid]:
17                    r = mid-1
18                else:
19                    l = mid+1
20        
21        return -1