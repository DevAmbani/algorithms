# Last updated: 6/26/2026, 9:01:46 AM
1from collections import defaultdict
2
3class Solution:
4    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
5        """
6        0 -> Unvisited
7        1 -> Visiting
8        2 -> Checked
9        """
10        state = [0] * numCourses
11        courseSchedule = defaultdict(list)
12        visited = []
13
14        for course, dependency in prerequisites:
15            courseSchedule[course].append(dependency)
16
17        def dfs(course):
18            if state[course] == 2:
19                return True
20            if state[course] == 1:
21                return False
22            
23            state[course] = 1
24
25            for dependency in courseSchedule[course]:
26                if dfs(dependency) is False:
27                    return False
28            
29            visited.append(course)
30            state[course] = 2
31        
32        for course in range(numCourses):
33            if dfs(course) is False:
34                return []
35        
36        return visited