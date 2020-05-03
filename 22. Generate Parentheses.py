from typing import List
import copy

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result_list = []

        def recursion(s='', left =0, right =0):
            if len(s) == 2*n: #if length of s is now satisfy the results length
                result_list.append(s)
                return
            if left < n: #we still need more left parenthesis
                recursion(s+"(", left+1, right)
            if left > right:
                recursion(s+")", left, right+1)

        recursion()
        return result_list



a = Solution()
print(a.generateParenthesis(3))