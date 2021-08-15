from collections import deque
n = int(input())
list_ = []

for i in range(n):
    temp_list = list(map(str, input()))
    list_.append(temp_list)


q = deque()

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def dfs(x,y):
    q = deque()

    q.append([x,y])
    list_[x][y] = "2"
    
    cnt = 1 
    while q:
        x,y = q.popleft()    
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if 0<= new_x <n and 0<= new_y < n:

                if list_[new_x][new_y] != "2" and list_[new_x][new_y] == "1":
                    q.append([new_x, new_y])
                    list_[new_x][new_y] = "2"
                    cnt += 1

    return cnt 

answer = []
answer_cnt = 0
for x in range(n):
    for y in range(n):
        if list_[x][y] != "0" and list_[x][y] != "2": #방문했는지, 검사 안해버리면 cnt 1 반환해버림
            cnt = dfs(x,y)
            answer_cnt += 1
            answer.append(cnt)

answer.sort()

print(answer_cnt)
for i in range(len(answer)):
    print(answer[i])