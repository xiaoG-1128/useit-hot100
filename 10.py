class Solution:
    def threeSum(self,nums):
        """

        :param nums:List[int]
        :return: List[List[int]]

        """
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2):
            if i>0 and nums[i]==nums[i-1]:
                continue

            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[rigth]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] ==nums[left + 1]:
                    left += 1
                while left < right and nums[right] ==nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
        return res