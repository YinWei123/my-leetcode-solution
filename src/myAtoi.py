class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        #去掉首尾空格
        s = s.strip()
        test = s
        num = ["-", "+", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for i in num:
            test = test.replace(unicode(i), '')

        if len(test) != 0:
            trash = test[0]
            s = s.split(trash)[0]
        if s:
            #考虑存在多个符号或者只有符号的情况
            if (s.count('+') + s.count('-') > 1) or ((s.count('+') + s.count('-') == 1) and len(s) == 1):
                return 0
            ret = int(s)
            if ret < -2147483648:
                return -2147483648
            elif ret > 2147483647:
                return 2147483647
            return ret
        return 0
