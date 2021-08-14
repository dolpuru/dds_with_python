from collections import deque
m, n = map(int, input().split())
list_ = []
for i in range(m):
    li = list(map(str, input()))
    list_.append(li)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()
q.append([0,0,0]) # x, y, cnt
list_[0][0] = "2"
def for_():
    while q:
        x,y, c = q.popleft()
        # list_[new_x][new_y] = "2" 여기서 체크를 하면 반복된 지점이 들어갈 수 있다. 
        if x == m-1 and y == n-1:
            return c + 1 
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if  0 <= new_x < m and 0<= new_y < n :
                if list_[new_x][new_y] != "2" and list_[new_x][new_y] == "1":
                    q.append([new_x, new_y, c + 1])
                    list_[new_x][new_y] = "2"


print(for_())