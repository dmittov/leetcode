from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_border = 0
        right_border = len(height) - 1
        best_volume = 0
        while left_border < right_border:
            left_hight = height[left_border]
            right_hight = height[right_border]
            container_hight = min(left_hight, right_hight)
            container_volume = container_hight * (right_border - left_border)
            if container_volume > best_volume:
                best_volume = container_volume
            if left_hight < right_hight:
                while (
                    height[left_border] <= container_hight
                    and left_border < right_border
                ):
                    left_border += 1
            else:
                while (
                    height[right_border] <= container_hight
                    and left_border < right_border
                ):
                    right_border -= 1
        return best_volume
