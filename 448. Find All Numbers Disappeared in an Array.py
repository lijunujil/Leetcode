from typing import List
from collections import defaultdict

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        possible_res = {i for i in range(1, len(nums)+1)}
        return list(possible_res - set(nums))


if __name__ == "__main__":
    a = Solution()
    print(a.findDisappearedNumbers([4,3,2,7,8,2,3,1]))