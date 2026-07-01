class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        some = set(nums)
        longest = 0 
        for num in some:
            # check if num is a start of a sequence:
            prev = num - 1
            if prev not in some:
                l = 1
            # creating the sequence:
            l = 1
            while num + l in some:
                l += 1
            longest = max(l, longest)

        return longest
            
        