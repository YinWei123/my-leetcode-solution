#coding : utf-8

class Solution(object):
    def longestPalindrome(self, s):
        """
        考虑奇偶两种情况，中心扩展
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s

        maxlen = 0
        start = 0
        # 偶数回文
        for index, item in enumerate(s):
            b = index
            a = index + 1
            while b >= 0 and a < len(s) and s[a] == s[b]:
                if a - b + 1 > maxlen:
                    maxlen = a - b + 1
                    start = b
                b -= 1
                a += 1

        # 奇数回文
        for index, item in enumerate(s):
            b = index - 1
            a = index + 1
            while b >= 0 and a < len(s) and s[a] == s[b]:
                if a - b + 1 > maxlen:
                    maxlen = a - b + 1
                    start = b
                b -= 1
                a += 1

        if maxlen == 0:
            return s[0]

        return s[start:start + maxlen]
