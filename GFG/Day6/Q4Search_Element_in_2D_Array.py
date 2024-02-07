###########Method1 (Linear Searching in rows and columns)
#T.C. = O(N)
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False


solution = Solution()
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
result = solution.searchMatrix(matrix, target)
print(result)


###Method 2 (Binary Search in 2D array)
#T.C. = O(log(m*n))