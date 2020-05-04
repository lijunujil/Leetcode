class Solution:
    def isHappy(self, n: int) -> bool:
        looped = set()
        while n != 1:
            n = sum([int(i)**2 for i in list(str(n))])
            if n in looped:
                return False

            looped.add(n)

        return True


sol = Solution()
# print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.isHappy(19))