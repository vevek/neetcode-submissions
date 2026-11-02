class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            if matrix[row][-1] < target:
                top = row + 1
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                break
        

        row = (top + bot) // 2

        lo, hi = 0, COLS - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if matrix[row][mid] < target:
                lo = mid + 1
            elif matrix[row][mid] > target:
                hi = mid - 1
            else:
                return True
        
        return False

