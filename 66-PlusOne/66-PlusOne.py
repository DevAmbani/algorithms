# Last updated: 2/6/2026, 4:50:49 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        num = 0
4        for k in digits:
5            num = num * 10 + k
6
7        num += 1
8        return list(map(int, str(num)))
9