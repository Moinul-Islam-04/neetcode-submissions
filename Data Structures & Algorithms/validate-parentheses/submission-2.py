class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        half = len(s) // 2

        if len(s) % 2 == 1:
            return False

        for i in range(half):
            stack.append(s[i])
        
        matching = {')': '(', '}': '{', ']': '['}

        for i in range(half, len(s)):
            if not stack:
                return False
            top = stack.pop()
            if matching.get(s[i]) != top:
                return False

        return len(stack) == 0