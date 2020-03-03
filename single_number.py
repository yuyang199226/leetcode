class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        init_num = nums[0]
        for i in range(1, len(nums)):
            init_num = init_num ^ nums[i]

        return init_num
