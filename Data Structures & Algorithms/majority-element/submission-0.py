class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # for this problem, we can just create a dictionary where the key is the num and the value is an increment

        n = len(nums)
        maj = {}

        for i in (nums):
            if i not in maj:
                maj[i] = 1
            else:
                maj[i] += 1
        
        return max(maj, key=maj.get)
