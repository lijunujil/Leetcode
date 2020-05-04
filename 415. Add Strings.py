class Solution:

    def addStrings(self, num1: str, num2: str) -> str:
        result_str = ""
        length1, length2 = len(num1), len(num2)
        max_length = max(length1, length2)

        carry_over = 0
        for pointer in range(-1, -(max_length+1), -1):
            int1 = int(num1[pointer]) if -pointer <= length1 else 0
            int2 = int(num2[pointer]) if -pointer <= length2 else 0

            curr_sum = int1 + int2 + carry_over
            result_str = str(curr_sum)[-1] + result_str

            carry_over = 1 if curr_sum >= 10 else 0

        if carry_over == 1:
            result_str = str(1) + result_str

        return result_str

sol = Solution()
# print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.addStrings('245', '8656'))