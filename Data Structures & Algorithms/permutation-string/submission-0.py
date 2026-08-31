class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        seen = {}
        mp = {}
        for s in s1:
            seen[s] = seen.get(s, 0) + 1
        
        for j, char in enumerate(s2):
            mp[char] = mp.get(char, 0) + 1 
        
            while j - i + 1 > len(s1):
                mp[s2[i]] = mp.get(s2[i]) - 1
                if mp[s2[i]] == 0:
                    del mp[s2[i]]
                i += 1

            if mp == seen:
                return True

        return False
        