from typing import List
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

# class Solution:
#     def singleNumber(self, nums: List[int]) -> int:
#         result = set()
#         for item in nums:
#             if item in result:
#                 result.remove(item)
#             else:
#                 result.add(item)
#         return result.pop()

if __name__ == "__main__":
    a = Solution()
    print(a.singleNumber([4,1,2,1,2]))
