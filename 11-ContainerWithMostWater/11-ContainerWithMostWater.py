# Last updated: 5/22/2026, 11:43:20 AM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        adder = []
4
5        for c in s:
6            if c == "(" or c == "{" or c == "[":
7                adder.append(c)
8            elif c == ")":
9                if not adder or adder[-1] != "(":
10                    return False
11                else:
12                    adder.pop()
13            elif c == "}": 
14                if not adder or adder[-1] != "{":
15                    return False
16                else:
17                    adder.pop()
18            elif c == "]": 
19                if not adder or adder[-1] != "[":
20                    return False
21                else:
22                    adder.pop()
23        
24        if len(adder) == 0:
25            return True
26        else:
27            return False
28