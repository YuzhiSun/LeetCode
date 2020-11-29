class Solution(object):
    def intersection(self, nums1: list, nums2: list) -> list:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        res = []
        for i in set1:
            if i in set2:
                res.append(i)
        return res
        # 更优化的方法
        # return list(set(nums1) & set(nums2))
    def intersection2(self, nums1: list, nums2: list) -> list:
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # set1 = set(nums1)
        # set2 = set(nums2)
        # res = []
        # for i in set1:
        #     if i in set2:
        #         for j in range(nums1.count(i) if nums1.count(i) < nums2.count(i) else nums2.count(i)):
        #             res.append(i)
        # return res
        res = []
        for i in list(set(nums1)&set(nums2)):
            for j in range(nums1.count(i) if nums1.count(i) < nums2.count(i) else nums2.count(i)):
                res.append(i)
        return res
# nums1 = [1,2,2,1]
# nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
so = Solution()
res = so.intersection2(nums1, nums2)
print(res)
