class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        hp = {}
        length = 0
        for j, char in enumerate(s):
            hp[char] = hp.get(char, 0) + 1
            maxfreq = max(hp.values())
            while (j-i+1) - maxfreq > k:
                hp[s[i]] = hp[s[i]] - 1
                i +=1
                maxfreq = max(hp.values())
            if (j-i+1) - maxfreq <= k:
                length = max(length, (j-i+1))


        return length