class Solution:
    def maxSum(self,intervals):
        if not intervals:
            return []

        intervals.sort()

        merged = []

        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
if __name__ == "__main__":
    n = int(input())
    intervals = [list(map(int,input().split()))for _ in range(n)]

    solution = Solution()
    result = solution.maxSum(intervals)

    for start, end in result:
        print(start, end)