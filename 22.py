class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        m,n = len(matrix),len(matrix[0])
        result = []

        top, bottom = 0, m-1
        left,right = 0, n-1

        