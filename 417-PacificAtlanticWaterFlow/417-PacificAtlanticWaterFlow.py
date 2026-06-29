# Last updated: 6/28/2026, 9:32:29 PM
1import heapq
2from collections import defaultdict
3
4class Solution:
5    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
6        graph = defaultdict(list)
7        dist = defaultdict(int)
8        
9        for u,v,w in times:
10            graph[u].append([v,w])
11
12        for i in (range(1, n+1)):
13            dist[i] = float('inf')
14        
15        dist[k] = 0
16
17        heap = [(0,k)]
18
19        while heap:
20            distance, node = heapq.heappop(heap)
21            if distance > dist[node]:
22                continue
23            
24            for neighbor, weight in graph[node]:
25                new_distance = dist[node] + weight
26                if new_distance < dist[neighbor]:
27                    dist[neighbor] = new_distance
28                    heapq.heappush(heap, (new_distance, neighbor))
29        
30        max_dist = max(dist.values())
31        return max_dist if max_dist < float('inf') else -1