class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix)-1

        row = -1

        while top<=bottom:
            row = (top+bottom)//2

            if target > matrix[row][-1]:
                top = row+1
            elif target < matrix[row][0]:
                bottom = row-1
            else:
                break

        if not (top <= bottom):
            return False
        else:
            l = 0
            u = len(matrix[row])-1
            mid = -1

            while l<=u:
                mid = (l+u)//2

                if matrix[row][mid] < target:
                    l = mid+1
                elif matrix[row][mid] > target:
                    u = mid-1
                else:
                    return True
            
            return False