class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        a = x ^ y
        res = 0
        while a > 0:
            if a & 1 == 1:
                res += 1
            a = a >> 1
        return res
