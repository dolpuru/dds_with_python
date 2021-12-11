from collections import deque
n = int(input())
painting = []
normal = 0
rg = 0
visited = [[False for i in range(n)] for j in range(n)]
x = [1,-1,0,0]
y = [0,0,-1,1]
for i in range(n):
    painting.append(list(input()))


def bfs(li,i,j,visited):  
    global n
    q = deque()
    q.append([i,j])
    visited[i][j] == True # 방문했으면 
    while q:
        a,b = q.popleft()
        for k in range(4):
            nx = a + x[k]
            ny = b + y[k]
            if 0<= nx <n and 0<= ny < n : 
                if visited[nx][ny] != True and li[nx][ny] == li[i][j]:
                    q.append([nx,ny])
                    visited[nx][ny] = True
    return 1



# 적록색맹 아닌 사람이 보는 구역의 개수2
for i in range(n):
    for j in range(n):
        if visited[i][j] == False: 
            normal += bfs(painting, i,j,visited)

#적록 색맹이 보는 그림 리 페인팅
for i in range(n):
    for j in range(n):
        visited[i][j] = False
        if painting[i][j] == 'R':
            painting[i][j] = 'G'
            

# 적록생맹이 보는 구역의 개수
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            rg += bfs(painting,i,j,visited)

print(normal,rg)