from collections import deque
n , m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int,input())))

answer = 0

def bfs(maze,i,j):
    global n,m
    q = deque()
    q.append((i,j))
    maze[i][j] = 0
    x = [1,-1,0,0]  
    y = [0,0,-1,1]
    
    while q:
        a,b = q.popleft()   
        for k in range(4):
            nx = a+x[k]
            ny = b+y[k]
            if 0> nx or n<= nx or 0>ny or m <=ny:
                continue
            if  maze[nx][ny] == 1:
                q.append((nx,ny))
                maze[nx][ny] = maze[a][b] + 1
                
    return maze[n-1][m-1]

answer = bfs(maze,0,0)
print(answer + 1)