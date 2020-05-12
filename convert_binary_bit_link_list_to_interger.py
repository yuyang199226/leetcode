class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        n = 0
        while head:
            n = (n << 1) | head.val
            head = head.next
        return n

