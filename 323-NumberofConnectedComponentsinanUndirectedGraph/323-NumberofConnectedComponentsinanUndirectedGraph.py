# Last updated: 6/30/2026, 6:44:24 AM
1import heapq
2from collections import defaultdict
3
4class Solution:
5    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
6        cost_graph = defaultdict(list)
7        dist = defaultdict(float)
8        for u,v,w in times:
9            cost_graph[u].append([v,w])
10        
11        for i in range(1, n+1):
12            dist[i] = float('inf')
13        dist[k] = 0
14
15        heap = [(0, k)]  # distance, node
16
17        while heap:
18            distance, node = heapq.heappop(heap)
19            if distance > dist[node]:
20                continue
21            
22            for neighbor, cost in cost_graph[node]:
23                n_dist = dist[node] + cost
24                if n_dist < dist[neighbor]:
25                    dist[neighbor] = n_dist
26                    heapq.heappush(heap,(n_dist, neighbor))
27        
28        ans = -1
29        for each in dist.values():
30            if each == float('inf'):
31                return -1
32            ans = max(ans, each)
33        
34        return ans
35