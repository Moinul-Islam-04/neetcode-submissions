class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)- 1

        i,j = 0, n

        while i < j:
            #Case 1: Letters are the same
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                #Case where values are not the same 
                # Need to check the Left (omitted) and right (omitted)
                left = s[i+1:j+1]
                right = s[i:j]

                return left == left[::-1] or right == right[::-1]

        return True