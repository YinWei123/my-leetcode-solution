#coding : utf-8

class Solution(object):
    def maxArea(self, height):
        """
        两边向中心移动，记录最大的面积，每次都移动high较短的一端
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        length = len(height)
        high = 0
        l = 0
        r = length - 1
        while l < r:
            if (min(height[l],height[r])*(r-l)) > max_area:
                max_area = min(height[l],height[r])*(r-l)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area