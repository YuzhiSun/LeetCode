class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        set_s = set(s)
        set_t = set(t)
        if set_s == set_t:
            for i in set_s:
                if s.count(i) == t.count(i):
                    continue
                else:
                    return False
            return True
        else:
            return False

s = "rat"
t = "car"
so = Solution()
res = so.isAnagram(s,t)
print(res)


