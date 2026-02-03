# Last updated: 2/3/2026, 2:46:49 PM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        slow, fast = 0, 0
4
5        while True:
6            slow = nums[slow]
7            fast = nums[fast]
8            fast = nums[fast]
9
10            if slow == fast:
11                break
12        
13        start = 0
14        while True:
15            start = nums[start]
16            slow = nums[slow]
17
18            if start == slow:
19                break
20        
21        return slow