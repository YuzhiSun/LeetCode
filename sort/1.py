class Solution(object):
    def twoSum(self, nums:list, target:int)->list :
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num],i]
            hashtable[num] = i
        return []

nums = [2, 7, 11, 15]
target = 9
so = Solution()
res = so.twoSum(nums, target)
print(res)