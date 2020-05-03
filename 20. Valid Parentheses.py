"""
use a stack, if it's open Parentheses, push into stack, if it's close Parentheses, pop from the stack
if there is no match Parentheses to pop or it's empty, meaning it's invalid
The return stack should be empty, meaning evert open Parentheses has a close Parentheses
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        else:
            stack = []
            mapping = {")": "(", "}": "{", "]": "["}
            for char in s:
                if char not in mapping.keys():
                    stack.append(char)
                elif len(stack) > 0 and mapping[char] in stack[-1]:
                    stack.pop()
                else:
                    return False
            return stack == []


if __name__ == "__main__":
    a = Solution()
    print(a.isValid("){"))
