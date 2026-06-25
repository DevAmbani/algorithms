# Last updated: 6/24/2026, 7:33:36 PM
1import heapq
2class MedianFinder:
3    def __init__(self):
4        self.arr = []
5
6    def addNum(self, num: int) -> None:
7        self.arr.append(num)
8
9    def findMedian(self) -> float:
10        self.arr.sort()
11        length = len(self.arr)
12        
13        if length % 2 != 0:
14            return float(self.arr[length // 2])
15        else:
16            mid = length // 2
17            return float((self.arr[mid] + self.arr[mid - 1]) / 2)
18        
19
20
21# Your MedianFinder object will be instantiated and called as such:
22# obj = MedianFinder()
23# obj.addNum(num)
24# param_2 = obj.findMedian()