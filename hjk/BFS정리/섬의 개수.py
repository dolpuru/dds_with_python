from collections import deque
import sys
input = sys.stdin.readline
def bfs(i, j):
    global n, h

    q = deque()
    q.append([i,j])
    list_[i][j] = 2
    x = [1,-1,0,0, 1,-1, 1,-1]
    y = [0,0,1,-1, 1, 1, -1,-1]

    while q:
        a, b = q.popleft()
        list_[a][b] = 2
        for k in range(8):
            if h > a + x[k] >= 0 and n > b + y[k] >= 0:
                # print("q = ",q)
                if list_[a + x[k]][b + y[k]] != 2 and list_[a + x[k]][b + y[k]] == 1:
                    list_[a + x[k]][b + y[k]] = 2
                    q.append([a + x[k], b + y[k]])

    return 1

while True:
    n, h = map(int,input().split())

    if n == 0 and h == 0:
        break
    
    list_ = [list(map(int,input().split())) for _ in range(h)]

    answer = 0

    for i in range(h):
        for j in range(n):
            if list_[i][j] == 2 or list_[i][j] == 0:
                continue
            answer += bfs(i, j)


    print(answer)