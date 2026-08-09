class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dic = {}
        res = []
        

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        print(dic)

        for keys in dic:
            if dic[keys] > (n/3):
                res.append(keys)

        return res