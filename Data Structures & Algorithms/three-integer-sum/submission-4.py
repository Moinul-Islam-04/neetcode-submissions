class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # the equation is a + b + c = 0
        # we can convert the equa to b + c = -a
        # so for the first example, we have -1 + 2 = -(-1) = 1 = 1 so that is a pair
        sorted_arr = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and sorted_arr[i] == sorted_arr[i-1]:   # skip duplicate fixed values
                continue

            j = i + 1
            k = len(nums) - 1
            target = -sorted_arr[i]
            while j < k:
                if sorted_arr[j] + sorted_arr[k] < target:
                    j += 1
                elif sorted_arr[j] + sorted_arr[k] > target:
                    k -=1
                else:
                    res.append([sorted_arr[i],sorted_arr[j],sorted_arr[k]])
                    j += 1
                    k -= 1
                    while j < k and sorted_arr[j] == sorted_arr[j-1]:   # skip duplicate pairs
                        j += 1

        return res
                







        
