class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        result = []

        # 定义边界
        top, bottom = 0, m - 1
        left, right = 0, n - 1

        while top <= bottom and left <= right:
            # 从左到右
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # 上边界下移

            # 从上到下
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # 右边界左移

            # 从右到左
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # 下边界上移

            # 从下到上
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # 左边界右移

        return result


# 读取输入
if __name__ == "__main__":
    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]
    solution = Solution()
    print(" ".join(map(str, solution.spiralOrder(matrix))))
