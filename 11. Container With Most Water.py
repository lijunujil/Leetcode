from typing import List
import numpy as np

class Solution:
    def maxArea(self, height: List[int]) -> int:
        pointer_left = 0
        pointer_right = len(height)-1

        # print(height[pointer_left], height[pointer_right])
        max_area = 0


        while pointer_right != pointer_left:
            curr_distance = pointer_right - pointer_left
            curr_height = min(height[pointer_left], height[pointer_right])
            curr_area = curr_distance * curr_height

            max_area = max(max_area, curr_area)

            if height[pointer_left] < height[pointer_right]:
                pointer_left += 1
            else:
                pointer_right -= 1

        return max_area

a = Solution()
a.maxArea(height = [1,8,6,2,5,4,8,3,7])
