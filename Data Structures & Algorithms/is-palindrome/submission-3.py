class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(char for char in s if char.isalnum()).lower()

        if new == " ":
            return True

        left = 0
        right = len(new) - 1


        while left < right:
            if new[left] == new[right]:
                left +=1
                right-=1
            if new[left] != new[right]:
                return False
            
        return True