from typing import List
import sys
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         min_price = sys.maxsize
#         max_profit = 0
#
#         for i in range(len(prices)):
#             if prices[i] < min_price:
#                 min_price = prices[i]
#             if prices[i] - min_price > max_profit:
#                 max_profit = prices[i] - min_price
#         return max_profit

class Solution:
    def maxProfit(self, prices):
        mn, mx = float("inf"), 0
        for i,v in enumerate(prices):
            mn, mx = min(mn, v), max(mx, v-mn)
        return mx

sol = Solution()
# print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([3,2,6,5,0,3]))