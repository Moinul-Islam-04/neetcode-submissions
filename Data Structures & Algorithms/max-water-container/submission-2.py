class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j, best = 0, len(heights) - 1, 0

        while i < j: 
            h = min(heights[i], heights[j])
            best = max(best, (h * (j-i)))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return best
        
        