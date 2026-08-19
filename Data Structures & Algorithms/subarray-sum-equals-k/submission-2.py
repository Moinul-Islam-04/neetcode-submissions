class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict = {0:1}
        prefix = 0
        res = 0

        for num in nums:
            prefix += num

            prev = prefix - k   
            if prev in mydict:
                res += mydict[prev]

            mydict[prefix] = mydict.get(prefix,0) + 1

        return res

