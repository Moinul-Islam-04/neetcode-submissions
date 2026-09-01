class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0, len(nums) - 1
        
        while i <= j:
            mid = (i+j) // 2
            if nums[mid] == target:
                    return mid

            if nums[i] <= nums[mid]:
                if nums[i] <= target <= nums[mid]:
                    j = mid - 1
                else: # target is greater than mid (on the right side)
                    i = mid + 1
            else:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else: # target is greater than mid (on the right side)
                    j = mid - 1


        return -1

                    



