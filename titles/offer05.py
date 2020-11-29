class Solution(object):
    def replaceSpace(self, s:str):
        """
        :type s: str
        :rtype: str
        """
        # 不知道为什么 提交是错的 结果是原字符串 后来知道了 需要选择python3版本
        # str_lst = list(s)
        # for i, el in enumerate(str_lst):
        #     if el is ' ':
        #         str_lst[i] = '%20'
        # s = "".join(str_lst)
        # return s
        str_lst = []
        for i in s:
            if i == ' ':
                str_lst.append('%20')
            else:
                str_lst.append(i)
        return "".join(str_lst)


s = "We are happy."
so = Solution()
res = so.replaceSpace(s)
print(res)