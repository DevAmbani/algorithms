# Last updated: 6/24/2026, 7:19:12 PM
1import heapq
2
3class Solution:
4    def lastStoneWeight(self, stones: List[int]) -> int:
5        heap = []
6
7        for i in range(len(stones)):
8            heapq.heappush(heap, -stones[i])
9        
10        while len(heap) > 1:
11            first = heapq.heappop(heap)
12            second = heapq.heappop(heap)
13
14            if first != second:
15                heapq.heappush(heap, first-second)
16        
17        if len(heap) == 0:
18            return 0
19        
20        return -heapq.heappop(heap)
21        