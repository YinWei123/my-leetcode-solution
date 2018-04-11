class Solution(object):
    def convert(self, s, numRows):
        """
        单纯的找规律
        :type s: str
        :type numRows: int
        :rtype: str
        """
        slen = len(s)
        if numRows == 1 or slen <= 1:
            return s
        zs = ''
        offset = 2 * numRows - 2
        i = 0
        j = 0
        while i < numRows:
            j = i
            while j < slen:
                zs += s[j]
                if i != 0 and i != numRows - 1 and j - 2 * i + offset < slen:
                    zs += s[j - 2 * i + offset]

                j += offset

            i += 1

        return zs
