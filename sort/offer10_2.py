class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 1, 1
        for _ in range(0,n):
            a, b = b, a+b
        return a % 1000000007