class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for char in operations:
            if char == "+":
                total = int(stack[-2]) + int(stack[-1])
                stack.append(total)
            elif char == "C":
                stack.pop()
            elif char == "D":
                num = int(stack[-1])
                stack.append(num*2)
            else:
                stack.append(int(char))
            
        return sum(stack)

        
        