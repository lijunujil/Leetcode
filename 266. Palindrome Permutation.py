from collections import Counter

# class Solution:
#     def canPermutePalindrome(self, s: str) -> bool:
#         char_count = Counter(s)
#         if len(s)/2 == 0:
#             return all([char_count[i]%2 == 0 for i in char_count])
#         else:
#             return sum([char_count[i]%2 == 0 for i in char_count]) >= len(char_count)-1

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        set_ = set()
        for char in s:
            set_.add(char) if char not in set_ else set_.remove(char)

        return len(set_) <= 1


if __name__ == "__main__":
    a = Solution()
    print(a.canPermutePalindrome("carerac"))
