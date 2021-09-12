#적록색약 , RG 구분 X
from collections import deque
n = int(input())
list_ = []
for i in range(n):
    temp = list(map(str, input()))
    list_.append(temp)

def bfs(key, x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n:
                if visited[new_x][new_y] == 0 and list_[new_x][new_y] == key:
                    q.append([new_x, new_y])
                    visited[new_x][new_y] = 1

def bfs_rg(key, x, y):
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if 0 <= new_x < n and 0 <= new_y < n:
                if visited[new_x][new_y] == 0 and list_[new_x][new_y] == key:
                    q.append([new_x, new_y])
                    visited[new_x][new_y] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] != 1:
            bfs(list_[i][j], i, j)
            cnt += 1
print(cnt, end = ' ')
#####################
cnt = 0
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if list_[i][j] == "R":
            list_[i][j] = "G"
            

for i in range(n):
    for j in range(n):
        if visited[i][j] != 1:
            bfs(list_[i][j], i, j)
            cnt += 1

print(cnt)