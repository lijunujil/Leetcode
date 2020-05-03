class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            returnVal = int(str(x)[::-1])
        else:
            returnVal = -1*int((str(x*-1)[::-1]))

        min = -2**31
        max = 2**31 -1

        if returnVal > max or returnVal< min:
            return 0
        else:
            return returnVal




if __name__ == "__main__":
    a = Solution()
    # print((123 % 10) * 10)
    print(a.reverse(73628123))