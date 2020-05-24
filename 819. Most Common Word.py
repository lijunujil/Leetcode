from typing import List

from collections import Counter
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        para_list = [i.lower() for i in re.findall("(\w*)\W*", paragraph)]
        count = Counter(para_list)
        for val in count.most_common():
            if val[0] not in banned:
                return val[0]

if __name__ == "__main__":
    a = Solution()
    print(a.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))