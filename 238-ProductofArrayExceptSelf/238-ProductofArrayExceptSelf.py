# Last updated: 5/18/2026, 9:59:11 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix, suffix = 1, 1
4        forward = [1] * len(nums)
5        reverse = [1] * len(nums)
6        ans = [1] * len(nums)
7
8        for i in range(len(nums)):
9            forward[i] = prefix
10            prefix *= nums[i]
11            
12
13        for i in range(len(nums)-1, -1, -1):
14            reverse[i] = suffix
15            suffix *= nums[i]
16            
17
18        for i in range(len(nums)):
19            ans[i] = forward[i] * reverse[i]
20
21        print(forward)
22        print(reverse)
23        return ans