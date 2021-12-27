from collections import deque

t = int(input())

def bfs(i,j,li,visited):
    global n, m
    if li[i][j] == 0 or visited[i][j] == True:
        return 0
    else:
        q = deque()
        q.append([i,j])
        visited[i][j] = True
        x = [1,-1,0,0,]
        y = [0,0,1,-1]
        while q:
            a,b = q.popleft()
            visited[a][b] = True
            for k in range(4):
                if 0 <= a+x[k] < n and 0 <= b+y[k] < m :
                    if li[a+x[k]][b+y[k]] == 1 and visited[a+x[k]][b+y[k]] == False:
                        q.append([a+x[k],b+y[k]])
                        visited[a+x[k]][b+y[k]] = True
        return 1

for  i in range(t):
    m , n , k = map(int,input().split())
    li = [ [0  for _ in  range(m)] for i in range(n) ]
    count = 0
    for i in range(k):
        x, y = map(int, input().split())
        li[y][x] = 1
    
    visited = [ [False  for _ in  range(m)] for i in range(n) ]
    for i in range(n):
        for j in range(m):
            count += bfs(i,j,li,visited)

    print(count)

