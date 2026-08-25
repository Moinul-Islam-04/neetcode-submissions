from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        i,j = 1, max(piles)

        while i < j:
            m = (i + j) // 2
            dur = 0
            for num in piles:
                dur += ceil(num/m)
            if dur <= h:
                j = m 
            else:
                i = m + 1
        
        return i

        