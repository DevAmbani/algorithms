# Last updated: 6/26/2026, 6:21:00 PM
1from collections import defaultdict, deque
2
3class Solution:
4    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
5        degrees = [0] * n
6        count = defaultdict(list)
7
8        if n==1:
9            return [0]
10
11        for a,b in edges:
12            count[a].append(b)
13            count[b].append(a)
14            degrees[a] += 1
15            degrees[b] += 1
16
17        queue = deque()
18        for i in range(len(degrees)):
19            if degrees[i] == 1:
20                queue.append(i)
21        
22        num_elements_left = n
23        while num_elements_left > 2:
24            num_elements_left = num_elements_left - len(queue)
25
26            for _ in range(len(queue)):
27                node = queue.popleft()
28
29                for neighbors in count[node]:
30                    degrees[neighbors] -= 1
31                    if degrees[neighbors] == 1:
32                        queue.append(neighbors)
33
34        return list(queue)
35        