from collections import deque

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
num = 0
for i in skill:
    if i[0] == 1:   #  공격
        for j in range(i[1],i[3]+1):
            for k in range(i[2],i[4]+1):
                board[j][k] -= i[5]
                
    else:               #  수비
        for j in range(i[1],i[3]+1):
            for k in range(i[2],i[4]+1):
                board[j][k] += + i[5]


def bfs(board, i,j):
    n = len(board)
    m = len(board[0])
    bd = 1
    q = deque()
    q.append((i,j))
    board[i][j] = 0
    x = [1,-1,0,0]
    y = [0,0,-1,1]
    while q:
        a, b = q.popleft()
        for k in range(4):
            nx = a + x[k]
            ny = b + y[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] > 0:
                board[nx][ny] = 0
                q.append((nx, ny))
                bd += 1
    return bd


for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] > 0 :
            num += bfs(board, i,j)
        
print(num)