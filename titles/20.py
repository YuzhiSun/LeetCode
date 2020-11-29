class Solution(object):
    def isValid(self, s: str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        hashtable = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stack = list()
        for ch in s:
            if ch in hashtable:
                if not stack or hashtable[ch] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

s = "()[]{}"
so = Solution()
res = so.isValid(s)
print(res)



