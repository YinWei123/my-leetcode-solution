#coding ： utf-8

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        比较取巧的合并了两个列表，并进行排序
        """

        nums1.extend(nums2)
        nums1 = sorted(nums1)

        if len(nums1) % 2 == 1:
            return nums1[len(nums1) / 2] / 1.0
        else:
            return (nums1[len(nums1) / 2] + nums1[len(nums1) / 2 - 1]) / 2.0