from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        mp = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            mp[key].append(s)
        return list(mp.values())

if __name__ == '__main__':
    n = int(input())
    strs = input().split()
    solution = Solution()
    ans = solution.groupAnagrams(strs)
    for group in ans:
        print(" ".join(group))
