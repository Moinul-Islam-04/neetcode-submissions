class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)

        nums.reverse()
        print(nums)

        def reverse(i,j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        

        #right side:
        reverse(k, len(nums) - 1)
        # left side
        reverse(0, k - 1)
        