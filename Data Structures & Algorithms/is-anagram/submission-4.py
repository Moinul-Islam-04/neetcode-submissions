class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        occur = {}

        if len(s) != len(t):
            return False
        for char in s:
            occur[char] = occur.get(char, 0) + 1
    
        for char in t:
            if char not in occur or occur[char] == 0:
                return False
            occur[char] -= 1
        
        return True