from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str):
        p_len, s_len = len(p), len(s)
        if s_len < p_len:
            return []

        # 记录 p 的字符计数
        p_count = Counter(p)
        s_count = Counter(s[:p_len])  # 统计第一个窗口的字符

        res = []
        if p_count == s_count:
            res.append(0)

        for i in range(p_len, s_len):
            # 新增字符
            s_count[s[i]] += 1
            # 移除窗口左端字符
            s_count[s[i - p_len]] -= 1
            if s_count[s[i - p_len]] == 0:
                del s_count[s[i - p_len]]

            # 检查窗口是否匹配
            if s_count == p_count:
                res.append(i - p_len + 1)

        return res

# 读取输入
s = input().strip()
p = input().strip()
solution = Solution()
result = solution.findAnagrams(s, p)
print(" ".join(map(str, result)))

