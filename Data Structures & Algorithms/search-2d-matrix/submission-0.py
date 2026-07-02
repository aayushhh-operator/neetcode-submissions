class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                break

        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True

        return False