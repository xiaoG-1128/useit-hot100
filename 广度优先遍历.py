from collections import deque

def bfs_maze(maze,start,end,n,m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[False] * m for _ in range(n)]
    q = deque()
    x1,y1 = start
    x2,y2 = end
    q.append((x1,y1))
    visited[x1][y1] = True

    while q:
        x,y = q.popleft()

        if (x,y)==(x2,y2):
            return True

        for i in range(4):
            new_x,new_y = x+dx[i], y+dy[i]

            if 0<=new_x<n and 0<=new_y<m and maze[new_x][new_y]==0 and not visited[new_x][new_y]:
                q.append((new_x,new_y))
                visited[new_x][new_y] = True

    return False

def main():
    n,m = map(int,input().split())
    maze = [list(map(int,input().split())) for _ in range(n)]
    x1,y1,x2,y2 = map(int,input().split())

    if maze[x1][y1] == 1 and maze[x2][y2] == 1:
        print("NO")
        return

    if bfs_maze(maze,(x1,y1),(x2,y2),n,m):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()