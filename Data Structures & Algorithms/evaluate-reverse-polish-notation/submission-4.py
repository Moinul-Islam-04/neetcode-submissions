class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for i, token in enumerate(tokens):
            if token == '+':
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = int(val1) + int(val2)
                stack.append(val3)
            elif token == '-':
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = int(val2) - int(val1)
                stack.append(val3)
            elif token == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                val3 = int(val1) * int(val2)
                stack.append(val3)
            elif token == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                if val1 == 0:
                    stack.append(0)
                val3 = int(val2) / int(val1)
                stack.append(int(val3))
            else:
                stack.append(int(tokens[i]))
        
        return stack.pop()
