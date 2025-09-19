class Solution:
    def longestConsecutive(self,nums):
        if not nums:
            return 0

        num_set = set(nums)
        longest_streak=0

        for num in num_set:
            if num-1 not in num_set:
                current_num=num
                current_streak=1

                while current_num+1 in num_set:
                    current_streak+=1
                    current_num+=1

                longest_streak=max(longest_streak,current_streak)

        return longest_streak

if __name__=='__main__':
    n=int(input().strip())
    nums = list(map(int,input().strip().split()))
    solution = Solution()
    print(solution.longestConsecutive(nums))