# Last updated: 6/26/2026, 8:34:12 AM
1from collections import defaultdict
2
3class Solution:
4    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
5        """
6        UNVISITED (0) → never been here
7        VISITING  (1) → currently in our DFS path (on the call stack)
8        VISITED   (2) → fully explored, confirmed no cycle below it
9        """
10        state = [0] * numCourses
11        courseSelection = defaultdict(list)
12
13        for course, depedency in prerequisites:
14            courseSelection[course].append(depedency)
15
16        def dfs(course):
17            if state[course] == 1:
18                return False
19            if state[course] == 2:
20                return True
21
22            state[course] = 1
23
24            for depedency in courseSelection[course]:
25                if dfs(depedency) is False:
26                    return False
27            
28            state[course] = 2
29            return True
30        
31        for course in range(numCourses):
32            if dfs(course) is False:
33                return False
34        
35        return True