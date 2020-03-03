# bit operation
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = []
        for i in s:
            n_i = ord(i)
            l.append(n_i)
        for j in t:
            l.append(ord(j))
        a = l[0]
        for i in range(1, len(l)):
            a = a ^ l[i]
        return chr(a)
