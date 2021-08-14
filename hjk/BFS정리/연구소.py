# 3중 for문으로 다 넣어봐야할듯 ?
# 먼저 벽 세우고 2로 물들이고, 나머지 0 카운트 넣고 
# 시간 신경쓰지말고 작성해보자.
import copy
# import sys
# input = sys.stdin.readline
from collections import deque
m, n = map(int, input().split(' '))

list_2 = []
for i in range(m):
    temp = list(map(int, input().split(' ')))
    list_2.append(temp)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(x,y):
    q = deque()
    q.append([x,y])
    list_[x][y] = 3 # 3은 방문했다는 표시
    while q:
        x,y = q.popleft()

        for i in range(4):

            new_x = x + dx[i]
            new_y = y + dy[i]
            if  new_x < 0 or new_y >= n or new_y < 0 or new_x >= m:
                continue

            elif list_[new_x][new_y] != 1 or list_[new_x][new_y] != 3:
                # 방문가능
                list_[new_x][new_y] = 3
                q.append([new_x,new_y])


wall_list = []
answer = 0
for i in range(m):
    for j in range(n):
        if list_2[i][j] == 0:

            for k in range(m):
                for l in range(n):

                    if list_2[k][l] == 0 and ( k != i or l != j):        
                        for p in range(m):
                            for o in range(n):
                                # 중복된 벽을 세우기에 초과했다.
                                if (i == k and j == l):
                                    continue

                                if (k == p and l == o):
                                    continue

                                if (p == i and o == j):
                                    continue

                                if list_2[k][l] == 0 and list_2[p][o] == 0 and list_2[i][j] == 0:

                                    if [[i,j],[k,l],[p,o]] in wall_list: # 넣어서 확인 하는 방식이 아니라 애초에 중복이 안되게 넣어야함 
                                        continue
                                    else:
                                        wall_list.append([[i,j],[k,l],[p,o]])

                                    list_ =  copy.deepcopy(list_2)
                                    list_[i][j] = 1
                                    list_[k][l] = 1
                                    list_[p][o] = 1
                                    
                                    for x in range(m):
                                        for y in range(n):
                                            if list_[x][y] == 2 and list_[x][y] != 3:
                                                bfs(x,y)

                                    cnt = 0
                                    for ee in range(m):
                                        for rr in range(n):
                                            if list_[ee][rr] == 0:
                                                cnt += 1
                                    answer = max( answer, cnt )
                    else:
                        continue
        else:
            continue

print(answer)

# 다른사람 풀이

# def wall(cnt):
#     if cnt == 3:
#         bfs()
#         return
#     for i in range(n):
#         for j in range(m):
#             if s[i][j] == 0:
#                 s[i][j] = 1
#                 wall(cnt + 1)
#                 s[i][j] = 0
# 보고 김틴힘 ㅋㅋ 