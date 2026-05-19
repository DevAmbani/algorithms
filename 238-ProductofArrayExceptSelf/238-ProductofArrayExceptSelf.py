# Last updated: 5/18/2026, 10:28:53 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count = defaultdict(int)
4
5        for n in nums:
6            count[n] += 1
7        
8        sorted_count = sorted(count.items(), key= lambda x: x[1], reverse=True)
9        ans = [item[0] for item in sorted_count]
10        finalans = ans[:k]
11
12        return finalans  