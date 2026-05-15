# Last updated: 5/14/2026, 10:26:32 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        final = defaultdict(list)
4
5        for word in strs:
6            key = tuple(sorted(word))
7            final[key].append(word)
8
9        return list(final.values())
10        
11        