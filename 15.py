class Solution:
    def subarraySum(self,nums,k):
        prefixSumCount={0:1}
        currentSum = 0
        count =0

        for num in nums:
            currentSum +=num

            if currentSum - k in prefixSumCount:
                count += prefixSumCount[currentSum - k]

            prefixSumCount[currentSum]= prefixSumCount.get(currentSum, 0)+1
        return count

if __name__ == '__main__':
    n,k = map(int,input().strip().split())
    nums = list(map(int,input().strip().split()))
    solution = Solution()
    print(solution.subarraySum(nums,k))