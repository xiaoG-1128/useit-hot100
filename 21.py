class Solution:
    def setZeroes(self,matrix):
        if not matrix:
            return

        m,n = len(matrix),len(matrix[0])
        row_zero = any(matrix[0][j] == 0 for j in range(n))
        col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] ==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j]=0

        if row_zero:
            for j in range(n):
                matrix[0][j] = 0

        if col_zero:
            for j in range(m):
                matrix[i][0] = 0

if __name__ == '__main__':
    m,n = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(m)]

    solution = Solution()
    solution.setZeroes(matrix)

    for row in matrix:
        print(" ".join(map(str,row)))