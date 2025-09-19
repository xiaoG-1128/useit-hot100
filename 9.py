class Solution:
    def maxArea(self,height):
        """
        :param height:List[int]
        :return:int
        """
        left,right = 0,len(height)-1
        max_area = 0

        while left < right:
            area = min(height[left],height[right])*(right-left)
            max_area = max(max_area,area)

            if height[left]<height[right]:
                left += 1
            else:
                right -= 1

        return max_area
if __name__ == "__main__":
    n = int(input())
    height = list(map(int,input().split()))
    solution = Solution()
    print(solution.maxArea(height))
