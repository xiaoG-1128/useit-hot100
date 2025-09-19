def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int,input().split()))for _ in range(n)]

    rotate(matrix)

    for row in matrix:
        print(" ".join(map(str,row)))
