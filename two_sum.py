# -*- coding: utf-8 -*-
# 1. two sum
# Given an array of integers, return indices of the
# two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.




class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, v in enumerate(nums):
            candidate = target - v

            if candidate in d:
                return [d[candidate], i]
            else:
                d[v] = i

# 2. Valid Parentheses

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


class Solution2(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == '':
            return True
        d = {'[': ']',
             '(': ')',
             '{': '}'}
        l = []
        for i in s:
            if i in d:
                l.append(i)
            else:
                if len(l) == 0 or d[l.pop()] != i:
                    return False
            return len(l) == 0

# 3 合并两个偏好序的列表

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution3(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur  = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        cur.next = l1 or l2
        return dummy.next










if __name__ == '__main__':
    pass
