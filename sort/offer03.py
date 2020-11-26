class Solution(object):
    def findRepeatNumber(self, nums:list):
        """
        :type nums: List[int]
        :rtype: int
        """
        # solution1
        # lst = []
        # for el in nums:
        #     if el in lst:
        #         return el
        #     else:
        #         lst.append(el)
        # solution2  # 注意题目提到了 数组长度为n 数值范围在n内 所以才可以用这个办法
        for index,el in enumerate(nums):
            while el != index:
                if el == nums[el]:
                    return el
                nums[el],nums[index] = el,nums[el]
        return -1



arr = [2, 3, 1, 0, 2, 5, 3]
so = Solution()
res = so.findRepeatNumber(arr)
print(res)