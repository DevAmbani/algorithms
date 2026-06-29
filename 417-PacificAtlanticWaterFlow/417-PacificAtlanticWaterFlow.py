# Last updated: 6/29/2026, 7:59:50 AM
1from collections import defaultdict
2
3class Solution:
4    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
5        dist = defaultdict(int)
6        
7        for i in range(n):
8            dist[i] = float('inf')
9        
10        dist[src] = 0
11
12        for i in range(k+1):
13
14            temp = dist.copy()
15            for source, dest, cost in flights:
16                new_dist = dist[source] + cost
17                if new_dist < temp[dest]:
18                    temp[dest] = new_dist
19            dist = temp
20        
21        if dist[dst] == float('inf'):
22            return -1
23        
24        return dist[dst]