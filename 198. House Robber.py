from typing import List

"""
DP solution:

Let us look at the case n = 1, clearly f(1) = A1.

Now, let us look at n = 2, which f(2) = max(A1, A2).

For n = 3, you have basically the following two options:

Rob the third house, and add its amount to the first house's amount.

Do not rob the third house, and stick with the maximum amount of the first two houses.

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        curr_max = 0
        previous_max = 0

        for _, val in enumerate(nums):
            temp_max = curr_max
            curr_max = max(previous_max + val, curr_max)
            previous_max = temp_max

        return curr_max



if __name__ == "__main__":
    a = Solution()
    print(a.rob([2,1,1,2]))