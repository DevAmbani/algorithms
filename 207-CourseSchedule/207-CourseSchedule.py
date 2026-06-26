# Last updated: 6/26/2026, 5:30:54 PM
1from collections import defaultdict, deque
2
3class Solution:
4    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
5        graph = defaultdict(list)        
6        indegree = [0] * numCourses      
7
8        for course, prereq in prerequisites:
9            graph[prereq].append(course)
10            indegree[course] += 1
11
12        queue = deque()                  
13        for i in range(numCourses):
14            if indegree[i] == 0:
15                queue.append(i)
16
17        result = []
18        while queue:
19            node = queue.popleft()
20            result.append(node)
21
22            for neighbor in graph[node]:
23                indegree[neighbor] -= 1
24                if indegree[neighbor] == 0:
25                    queue.append(neighbor)
26
27        return len(result) == numCourses