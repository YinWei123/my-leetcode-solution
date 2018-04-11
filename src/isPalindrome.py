#coding ： utf-8

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        区分奇偶，和判断最长回文子串方法一致
        中心扩展
        """
        s = str(x)
        ret = True

        if s.find('-', None) is None:
            return False

        slen = len(s)
        if slen < 2:
            return True

        # 偶数回文
        if slen % 2 == 0:
            h = slen / 2 - 1
            l = slen / 2
            while h >= 0:
                if s[h] != s[l]:
                    ret = False
                    break
                h -= 1
                l += 1
            return ret

        # 奇数回文
        if slen % 2 == 1:
            h = slen / 2 - 1
            l = slen / 2 + 1
            while h >= 0:
                if s[h] != s[l]:
                    ret = False
                    break
                h -= 1
                l += 1
            return ret