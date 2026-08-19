class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #array is not sorted so i firstly we should sort the array
        # we need to decide the B/H rate which is K, which I assume is going to be our middle value


        # i is going to be the lowest value our array can be, l will be our highest value in the array
        def ciel(num, m):
           return (num + m - 1) // m


        i,j = 1, max(piles)
        current = max(piles)
        while i <= j:  
            m = (i + j) // 2

            hours = sum(ciel(pile, m) for pile in piles)

            if hours > h:
                i = m + 1
            elif hours <= h:
                j = m - 1
                current = m

        return current    

        

        