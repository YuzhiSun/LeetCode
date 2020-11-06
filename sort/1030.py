class Solution(object):
    def allCellsDistOrder(self, R:int, C:int, r0:int, c0:int):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        lst = [[i, j] for i in range(R) for j in range(C)]
        lst.sort(key=lambda x:abs(x[0]-r0) + abs(x[1]-c0))
        return lst










R = 2
C = 3
r0 = 1
c0 = 2

so = Solution()
res = so.allCellsDistOrder(R, C, r0, c0)
print(res)