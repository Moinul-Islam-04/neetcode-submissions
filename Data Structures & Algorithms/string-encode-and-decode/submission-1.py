class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            num = len(s)
            res += str(num) + '#' + s
        print(res)
        return res
    

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # gives us the number 
            begin = j + 1
            res.append(s[begin:begin + length])
            
            i = begin + length
        return res

                    


        


