class Solution(object):
    def largestPerimeter(self, A : list) -> int:
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        for i in range(len(A) - 2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0

lst = [3,2,3,4]
so = Solution()
res = so.largestPerimeter(lst)
print(res)