# Last updated: 6/30/2026, 7:23:49 AM
1from collections import defaultdict
2
3class Solution:
4    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
5        dist = defaultdict(int)
6        for i in range(n):
7            dist[i] = float('inf')
8        dist[src] = 0
9
10        for _ in range(k+1):
11            temp = dist.copy()
12            for sour, dest, cost in flights:
13                if temp[dest] > dist[sour] + cost:
14                    temp[dest] = dist[sour] + cost
15            dist = temp
16
17        if dist[dst] == float('inf'):
18            return -1
19        return dist[dst]