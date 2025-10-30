# Last updated: 10/30/2025, 12:57:24 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxlen = 0
        seen = set()

        for r in range(0, len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen