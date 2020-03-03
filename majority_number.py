class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        e = nums[0]
        for i in range(1, len(nums)):
            if count == 0:
                e = nums[i]
                count = 1
                continue
            if nums[i] == e:
                count += 1
            else:
                count -= 1

        return e
