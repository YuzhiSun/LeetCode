class Solution(object):
    def sortArrayByParityII(self, A:list) -> list:
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res_lst = [i for i in range(len(A))]
        i = 0 # 代表偶数
        j = 1 # 代表奇数
        for ele in A:
            if ele % 2 == 0:
                res_lst[i] = ele
                i += 2
            else:
                res_lst[j] = ele
                j += 2
        return res_lst


A = [4,2,5,7]
so = Solution()
res = so.sortArrayByParityII(A)
print(res)
