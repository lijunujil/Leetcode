from typing import List


class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        count = defaultdict(int)
        for item in cpdomains:
            times, domains = item.split(" ")

            while len(domains) >0:
                count[domains] += int(times)
                domains = ".".join(domains.split(".")[1:])

        return ([" ".join([str(value), key]) for key, value in count.items()])


if __name__ == "__main__":
    a = Solution()
    print(a.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
