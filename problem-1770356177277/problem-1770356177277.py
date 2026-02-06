# Last updated: 2/5/2026, 11:36:17 PM
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x == 0:
4            return 0
5        if x == 1:
6            return 1
7        for i in range(0,x+1):
8            if (i*i) > x:
9                return i-1
10            elif (i*i) == x:
11                return i