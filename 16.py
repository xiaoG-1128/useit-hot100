from collections import deque
import sys
from sys import stdlib_module_names


class Solution:
    def maxSlidingWindow(self,num,k):
        deque_window = deque()
        result = []

        for i in range(len(nums)):
            if deque_window and deque_window[0]<i-k+1:
                deque_window.popleft()

            while deque_window and nums[deque_window[-1]]< nums[i]:
                deque_window.pop()

            deque_window.append(i)

            if i>=k-1:
                result.append(nums[deque_window[0]])
        return result

if __name__ == '__main__':
    n,k = map(int,sys.stdin.readline().split())
    nums = list(map(int,sys.stdin.readline().split()))

    solution =Solution()
    result = solution.maxSlidingWindow(nums,k)

    print(" ".join(map(str,result)))