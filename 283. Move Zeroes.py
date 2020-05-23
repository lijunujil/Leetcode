from typing import List


# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         zero_pointer = 0
#         for idx in range(len(nums)):
#             if nums[idx] == 0 and nums[zero_pointer] != 0: #assign 0 pointer if it's not point to 0 and current value is 0
#                 zero_pointer = idx
#             if nums[idx] != 0: # swap value with 0 pointer if current val is not 0
#                 nums[idx], nums[zero_pointer] = nums[zero_pointer], nums[idx]
#                 zero_pointer +=1 #move o pinter to next idx, to be determine if it's a 0 pointer at that idx
#             print(nums)

class Solution(object):
    def moveZeroes(self, nums):
        """
        We initialize two pointers i = 0, j = 0. Iterate j over range(len(nums)), and if nums[j] != 0, we swap nums[i] and nums[j], and increment i by 1. It is easy to see the loop invariant that nums[:i+1] contains all nonzero elements in nums[:j+1] with relative order preserved. Hence when j reaches len(nums)-1, nums[:i+1] contains all nonzero elements in nums with relative order preserved.

Time complexity: O(n), space complexity: O(1).
        """
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            print(nums)

if __name__ == "__main__":
    a = Solution()
    # nums = [0,1,0,3,12]
    nums = [1,0,3,4,5]

    a.moveZeroes(nums)

