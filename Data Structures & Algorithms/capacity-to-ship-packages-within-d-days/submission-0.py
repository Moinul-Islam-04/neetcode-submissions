class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i,j = max(weights), sum(weights)

        while i < j:
            time, load = 1, 0
            m = (i+j) // 2
            for weight in weights:
                if load + weight > m:
                    load = weight
                    time += 1
                else:
                    load += weight
            
            if time <= days:
                j = m
            else:
                i = m + 1
        
        return j