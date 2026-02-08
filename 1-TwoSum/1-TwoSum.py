# Last updated: 2/8/2026, 4:07:24 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3
4        for num1 in range(len(nums)):
5            for num2 in range(num1+1, len(nums)):
6                if (nums[num1]+nums[num2] == target):
7                    sln = [num1, num2]
8                    break
9
10        return sln