class Solution:
    def maxSubArray(self,nums):
        maxSum = float('-inf')
        currentSum = 0

        for num in nums:
            currentSum =max(num,currentSum+num)
            maxSum = max(maxSum,currentSum)

        return maxSum

if __name__ == '__main__':
    n = int(input().strip())
    nums = list(map(int,input().split))

    solution = Solution()
    print(solution.maxSubArray(nums))