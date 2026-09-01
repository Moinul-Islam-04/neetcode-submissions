class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        res = 0
        length = len(nums) + 1
        print(length)

        for j, num in enumerate(nums):
            res += num
            while res >= target:
                res -= nums[i]
                length = min(length, j-i+1)
                i += 1
            
        if length == len(nums) + 1:
            return 0
           



        return length
