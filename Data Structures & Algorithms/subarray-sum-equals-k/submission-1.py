class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict = {}
        n = len(nums)
        prefix = [0] * (n+1)
        res = 0

        for i in range(1, n+1):
            prefix[i] = prefix[i-1] + nums[i-1]
        print(prefix)


        for curr in prefix:
            prev = curr - k
            if prev in mydict:
                res += mydict[prev]

            mydict[curr] = mydict.get(curr,0) + 1

        return res
