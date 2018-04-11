#coding ： utf-8

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        顺序遍历子串，
        通过字典map记录字符出现的次数
        出现超过一次，跳出循环并与
        最大长度比较。
        """
        map = {}
        max_len = 0
        strlen = len(s)
        if strlen == 1:
            return 1
        for index, item in enumerate(s):
            map[s[index]] = 1
            i = index + 1
            while i < strlen:
                if map.get(s[i], -1) == -1:
                    map[s[i]] = 1
                else:
                    if max_len < (i-index):
                        max_len = i - index
                    break
                i += 1
            if i == strlen and (i-index) > max_len:
                max_len = i - index

            map.clear()
        return max_len