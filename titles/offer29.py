class Solution(object):
    def __init__(self):
        pass
    def spiralOrder(self, matrix:list):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        rows, cols = len(matrix),len(matrix[0])
        if rows == 0 or cols == 0:
            return []
        while matrix:
            res.extend((matrix[0]))
            matrix = self.transpose(matrix)
        return res
    def transpose(self,matrix):
        rows, cols = len(matrix), len(matrix[0])
        matrix_r = []
        for c in range(0,cols):
            c_tmp = []
            for r in range(1,rows):
                c_tmp.append(matrix[r][cols -1 - c])
            matrix_r.append(c_tmp)
        # print(matrix,matrix_r)
        return matrix_r


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix1 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12]]
so = Solution()
res = so.spiralOrder(matrix1)
print(res)