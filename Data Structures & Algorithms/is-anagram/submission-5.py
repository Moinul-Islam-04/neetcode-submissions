class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # need a dict, where key is a letter and value is occurance of letter
        res = {}

        #check if s and t are same lenght

        if len(s) != len(t):
            return False
        
        for c in s:
            res[c] = res.get(c, 0) + 1
        
        for c in t:
            if c not in res or res[c] == 0:
                return False
            res[c] -=1

        return True
                
        