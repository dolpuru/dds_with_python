from collections import deque

m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


def bfs(i,j,s,visited,board,n,m):
    count = 1
    q = deque()
    q.append((i,j))
    visited[i][j] = 1
    board[i][j] = 0
    x = [1,-1,0,0]
    y = [0,0,-1,1]
    while q:
        a, b = q.popleft()
        for k in range(4):
            nx = a + x[k]
            ny = b + y[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:  continue
            if visited[nx][ny] != 1:
                visited[nx][ny] = 1
                if s == board[nx][ny]:  
                    count += 1
                    board[i][j] = 0
                    q.append((nx,ny))
    return count


for i in range(m):
    board[i] = list(board[i])
print(board)

answer = 0
while 1:
    visited = [[0 for i in range(n)] for i in range(m)]
    temp = 0
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j] == board[i+1][j] == board[i][j+1] == board[i+1][j+1]:
                temp = bfs(i,j,board[i][j],visited,board,n,m)
                answer += temp
    if temp == 1:   break
    else:
        
print(answer)