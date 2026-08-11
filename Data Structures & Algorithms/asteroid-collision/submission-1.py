class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for nums in asteroids:
            alive = True

            while stack and nums < 0 < stack[-1]:

                if stack[-1] < abs(nums):
                    stack.pop()
                    continue
                elif stack[-1] == abs(nums):
                    stack.pop()
                    alive = False
                    break
                else:
                    alife = False
                    break
            else:
                stack.append(nums)
            

        return stack