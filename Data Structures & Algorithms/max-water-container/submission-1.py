class Solution:
    def maxArea(self, heights: List[int]) -> int:

        j,k, target = 0, len(heights) - 1, 0

        while j < k:
            h,w = 0,0
            h = min(heights[j],heights[k]) #highest it can be
            w = k - j 

            target = max(target, (h * w))
            if heights[j] < heights[k]:
                j += 1
            else:
                k -= 1
            
            
           

        return target
        

        