#devide and conqur solution

class Solution:
    def findLCP(self, strs):
        if len(strs) == 1:
            return strs[0]
        elif len(strs) == 2:
            returnstrs = ""
            minIdx = min(len(strs[0]), len(strs[1]))
            for idx in range(minIdx):
                if strs[0][idx] == strs[1][idx]:
                    returnstrs += strs[0][idx]
                else:
                    break
            return returnstrs
        else:
            return ""

    def longestCommonPrefix(self, strs) -> str:
        listLength = len(strs)
        if listLength <= 2:
            return self.findLCP(strs)
        else:
            lefthalf = strs[:int(listLength/2)]
            righthalf = strs[int(listLength/2):]
            leftLCP = self.longestCommonPrefix(lefthalf)
            rightLCP = self.longestCommonPrefix(righthalf)
            LCP = self.findLCP([leftLCP, rightLCP])
            return LCP



if __name__ == "__main__":
    a = Solution()
    print(a.longestCommonPrefix(["ca","a"]))

    # strs = ["leetcode", "leet", "lee", "le", "ji"]
    # listLength = len(strs)
    # print(strs[:int(listLength/2)],strs[int(listLength/2):])