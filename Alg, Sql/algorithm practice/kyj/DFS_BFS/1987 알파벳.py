from collections import deque
answer = 0
r,c = map(int,input().split())
li = []
for i in range(r):
    li.append(list(input()))

alp = [False] * 26
# A= 97
x = [1,-1,0,0]
y = [0,0,-1,1]
result = []

def bfs(i,j):
    global r,c,answer
    count = 0
    q = deque()
    q.append([i,j])
    temp = li[i][j]
    alp[90-ord(temp)] = True
    li[i][j] = 0
    
    while q:
        a,b = q.popleft()
        for k in range(4):
            nx = a + x[k]
            ny = b + y[k]
            if 0<= nx < r and 0<= ny < c and li[nx][ny] !=0:
                temp = li[nx][ny]
                if alp[90-ord(temp)] == False:
                    q.append([nx,ny])
                    li[nx][ny] = 0
                    alp[90-ord(temp)] = True
                    answer += 1
    return answer
for i in range(r):
    for j in range(c):
        if li[i][j] != 0 :
            result.append(bfs(i,j))

print(max(result))