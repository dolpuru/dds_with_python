from collections import deque
n = int(input())
estate = []
for i in range(n):
    estate.append(list(map(int,input())))
house_n = []

def bfs(estate, i,j):
    global n
    house = 1
    q = deque()
    q.append((i,j))
    estate[i][j] = 0
    x = [1,-1,0,0]
    y = [0,0,-1,1]
    while q:
        a, b = q.popleft()
        for k in range(4):
            nx = a + x[k]
            ny = b + y[k]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if estate[nx][ny] == 1:
                estate[nx][ny] = 0
                q.append((nx, ny))
                house += 1
    return house
                



for i in range(n):
    for j in range(n):
        if estate[i][j] == 1 :
            house_n.append(bfs(estate, i,j))

house_n.sort()
print(len(house_n))
for i in house_n:
    print(i)