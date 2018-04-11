#coding: utf-8

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        找到长度最小的字符串
        再判断
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        min_len = len(strs[0])
        min_str = strs[0]
        max_len = 0
        for str in strs[1:]:
            if len(str) < min_len:
                min_len = len(str)
                min_str = str
            if min_len == 0:
                return ''
        max_len = min_len
        print(min_len, min_str)
        for str in strs:
            i = max_len
            while i > 0:
                if str[:i] == min_str[:i]:
                    if i < max_len:
                        max_len = i
                    break
                elif i == 1:
                    return ''
                i -= 1
        return min_str[:max_len]


