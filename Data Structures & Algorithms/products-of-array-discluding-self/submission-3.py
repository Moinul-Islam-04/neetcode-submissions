class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
       
        prefix = [1] * n #gives us an array of 0s

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        suff = [1] * n
      
        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]
        

        result = [prefix[i] * suff[i] for i in range(n)]

        return(result)
           