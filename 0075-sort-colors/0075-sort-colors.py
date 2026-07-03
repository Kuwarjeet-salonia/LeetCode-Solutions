class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        max_value = max(nums)
        count  = [0] * (max_value + 1)
        

        n = len(nums)
        for i in range(n-1):
            for j in range(n-1-i):
                if nums[j+1] < nums[j]:
                   nums[j], nums[j+1] = nums[j+1],nums[j]
        return nums
