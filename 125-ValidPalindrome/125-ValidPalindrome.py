# Last updated: 5/21/2026, 3:08:24 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        sorted_nums = sorted(nums)
4        ans = []
5        seen = set()
6
7        for i in range(len(sorted_nums)-2):
8            l = i+1
9            r = len(sorted_nums) - 1
10            n = sorted_nums[i]
11
12            while l < r:
13                total = sorted_nums[l] + sorted_nums[r] + n
14                
15                if total == 0:
16                    adder = [n, sorted_nums[l], sorted_nums[r]]
17                    if tuple(adder) not in seen:
18                        seen.add(tuple(adder))
19                        ans.append(adder)
20                    l += 1
21                    r -= 1
22                elif total < 0:
23                    l += 1
24                elif total > 0:
25                    r -= 1
26            
27        return ans