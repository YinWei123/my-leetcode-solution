#coding : utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        使用了 list 的 index 方法
        """
        for index, item in enumerate(nums):
            tar = target - item
            try:
                posi = nums.index(tar)
                if posi != index:
                    return sorted([index, posi])
            except ValueError:
                pass

