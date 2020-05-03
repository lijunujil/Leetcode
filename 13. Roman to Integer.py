class Solution:
    def __init__(self):
        self.map = {"I": 1, "V": 5, "X": 10, "L": 50, "C":100, "D":500, "M": 1000}
    def romanToInt(self, s: str) -> int:
        Val = 0
        previous = 0

        for char in s[::-1]:
            temp = self.map[char]
            if temp < previous:
                Val -= temp
            else:
                Val += temp
            previous = temp

        return Val

if __name__ == "__main__":
    a = Solution()
    # print((123 % 10) * 10)
    print(a.romanToInt("IV"))