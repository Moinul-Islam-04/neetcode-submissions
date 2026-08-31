class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j = 0,0
        length = 0
        seen = {}

        for j, char in enumerate(s):
            if char in seen and seen[char] >= i:
                i = seen[char] + 1
            
            seen[char] = j
            length = max(length, (j-i+1))

        return length