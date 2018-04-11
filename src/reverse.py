#coding : utf-8

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x).replace('-', '')
        s = s[::-1]

        if x < 0:
            s = '-{}'.format(s)

        x = int(s)

        if x > 2 ** 31 or x < -(2 ** 31):
            return 0

        return x