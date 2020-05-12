class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        f = head
        s = head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False
