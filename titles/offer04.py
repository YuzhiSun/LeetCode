class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        col, row =len(matrix[0]) - 1, 0
        row_max = len(matrix) - 1
        if row_max == 0:
            while col >=0 :
                if target == matrix[0][col]:
                    return True
                elif target < matrix[0][col]:
                    col -= 1
                    continue
                elif target > matrix[0][col]:
                    return False


        while (row <= row_max) & (col >=0 ):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -=1
                continue
            elif matrix[row][col] < target:
                row += 1
                continue
            else:
                return False
        return False


matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

target1 = 5
target2 = 20
emp = []
so = Solution()
res = so.findNumberIn2DArray([[-1],[-1]],0)
print(res)
