from collections import deque

def bfs(i, j):
    global n, h
    if list_[i][j] == 0 or visited[i][j] == 1:
        return 0
    else:
        
        q = deque()
        q.append([i,j])
        x = [1,-1,0,0, 1,-1, 1,-1]
        y = [0,0,1,-1, 1, 1, -1,-1]
        visited[i][j] = 1
        while q:
            a, b = q.popleft()
            visited[a][b] = 1
            for k in range(8):
                try:
                    # print("q = ",q)
                    if list_[a + x[k]][b + y[k]] == 1 and visited[a + x[k]][b + y[k]] == 0:
                        visited[a + x[k]][b + y[k]] == 1
                        q.append(a + x[k], b + y[k])
                        print([a+x[k], b+y[k]])
                except:
                    pass
        return 1

while True:
    n, h = map(int,input().split())

    if n == 0 and h == 0:
        break
    
    list_ = [list(map(int,input().split())) for _ in range(h)]
    visited = [[0 for _ in range(n)] for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(n):
            answer += bfs(i, j)


    print(answer)