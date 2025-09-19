class Solution:
    def twoSum(self,nums,target):
        num_to_index = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

n,target = map(int,input().split())
nums = list(map(int,input().split()))

solution = Solution()
result = solution.twoSum(nums,target)

print(result[0], result[1])
