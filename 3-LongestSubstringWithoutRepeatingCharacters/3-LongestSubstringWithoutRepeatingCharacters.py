# Last updated: 10/31/2025, 11:47:13 AM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        s2_count = {}
        for k in range(len(s1)):
            s1_count[s1[k]] = 1 + s1_count.get(s1[k], 0)

        window = len(s1)
        l = 0
        for r in range(len(s2)):
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)

            if r - l + 1 > window:
                s2_count[s2[l]] -= 1

                if s2_count[s2[l]] == 0:
                    del s2_count[s2[l]]
                    
                l += 1
            
            if s1_count == s2_count:
                return True
        return False