from collections import deque
def bfs(i,j,li,visited):
    global w,h
    if li[i][j] == 0 or visited[i][j] == True:
        return 0
    else :
        q = deque()
        q.append([i,j])
        x = [1,-1,0,0,-1,1,-1,1]
        y = [0,0,-1,1,1,1,-1,-1]
        visited[i][j] = True
        while q:
            a, b = q.popleft()
            visited[a][b] = True
            for k in range(8):
                if a + x[k] < 0 or b + y[k] < 0 or a + x[k] >= h or b + y[k] >= w:
                    continue
                else:
                    if li[a + x[k]][b + y[k]] == 1 and visited[a + x[k]][b + y[k]] == False:
                        visited[a + x[k]][b + y[k]] = True
                        q.append([a + x[k], b + y[k]])

        return 1

while(1):
    w,h = map(int, input().split())

    if w == 0 and h==0:
        break
        
    li = [list(map(int, input().split())) for i in range(h)]
    visited = [[False for i in range(w)] for j in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            answer += bfs(i,j,li,visited)
    
    print(answer)

