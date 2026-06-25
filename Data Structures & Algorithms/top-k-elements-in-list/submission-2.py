class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        array = []

        for num in nums:
            res[num] = res.get(num, 0) + 1
        
        print(res)
        #sorted_desc = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

        #array.extend(list(sorted_desc.keys())[:k])
        return sorted(res, key=res.get, reverse=True)[:k]



        