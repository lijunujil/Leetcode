# import re
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         retrived = re.findall("\w", s)
#         left, right = 0, len(retrived)-1
#         while left <= right:
#             if retrived[left].lower() != retrived[right].lower():
#                 return False
#             left, right = left + 1, right -1
#         return True

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        retrived = "".join(re.findall("\w", s)).lower()
        return retrived == retrived[::-1]


if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome("race a car"))
