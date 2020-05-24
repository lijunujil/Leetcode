from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = defaultdict(lambda: 0)
        for char in s:
            hash_map[char] += 1
        for idx in range(len(s)):
            if hash_map[s[idx]] == 1:
                return idx
        return -1

if __name__ == "__main__":
    a = Solution()
    print(a.firstUniqChar("loveleetcode"))