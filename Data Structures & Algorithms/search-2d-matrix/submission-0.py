class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        

        left = 0
        right = (row * col) - 1
       
        while left <= right:
            mid = left + (right - left) // 2

            row_idx = mid // col
            col_idx = mid % col

            curr = matrix[row_idx][col_idx]
            print(curr)

            if curr > target:
                right = mid -  1
            elif curr < target:
                left = mid + 1
            elif curr == target:
                return True
        return False
