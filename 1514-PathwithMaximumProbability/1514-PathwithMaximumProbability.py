# Last updated: 6/29/2026, 8:33:37 AM
1from collections import defaultdict
2import heapq
3
4class Solution:
5    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
6        cost_graph = defaultdict(list)
7        dist = defaultdict(int)
8        count = 0
9
10        for u,v in edges:
11            cost_graph[u].append([v, succProb[count]])
12            cost_graph[v].append([u, succProb[count]])
13            dist[count] = 0
14            count += 1
15        
16        dist[start_node] = 1
17
18        neighbor_heap = [(-1, start_node)]
19
20        while neighbor_heap:
21            distance, node = heapq.heappop(neighbor_heap)
22            distance = -distance
23
24            if distance < dist[node]:
25                continue
26            
27            for neighbor, cost in cost_graph[node]:
28                new_dist = dist[node] * cost
29                if new_dist > dist[neighbor]:
30                    dist[neighbor] = new_dist
31                    heapq.heappush(neighbor_heap, (-new_dist, neighbor))
32            
33        return dist[end_node]
34