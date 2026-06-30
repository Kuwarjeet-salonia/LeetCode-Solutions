class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        merged = len(nums)
        if merged % 2 == 1 :
            return nums[merged//2]
        else : 
            return (nums[merged//2] + nums[(merged//2)-1])/2.0