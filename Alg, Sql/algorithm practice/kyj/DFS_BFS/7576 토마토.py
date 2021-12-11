from collections import deque
m,n = map(int,input().split())
box = []
li = []

for i in range(n):
    box.append(list(map(int,input().split())))
    for j in range(m):
        if box[i][j] == 1:
            li.append([i,j])

x = [1,-1,0,0]
y = [0,0,-1,1]


q = deque()
nice_to = len(li)
for i,j in li:
    q.append([i,j])

while q:
    a,b = q.popleft()
    for k in range(4):
        nx = a + x[k]
        ny = b + y[k]
        if 0<= nx < n and 0<= ny < m:
            if box[nx][ny] == 0:
                q.append([nx,ny])
                if box[nx][ny] != -1:
                    box[nx][ny] = box[a][b] + 1


for i in range(n):
    for j in range(m):
        if box[i][j] ==0:
            print(-1)
            exit()

if box[a][b] == 1:
    print(0)
else:
    print(box[a][b]-1)



