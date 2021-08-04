from collections import deque

def dfs(li,V,visited):
    #현재 노드 방문 처리
    visited[V] = 1
    print(V, end = ' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in li[V]:
        if visited[i] == 0:
            dfs(li,i,visited)

def bfs(li,V,visited):
    deq = deque([V])
    visited[V] = 0

    while deq: # 큐가 빌때 까지
        #맨 처음 인자 빼고, 출력
        V = deq.popleft()
        print(V, end = ' ')
        #방문하지 않은 인자 큐에 추가
        for i in li[V]:
            if visited[i] == 1:
                deq.append(i)
                visited[i] = 0


N, M, V = map(int, input().split())

li = [[]for i in range(N+1)]

for i in range(M):
    num_1, num_2 = map(int, input().split())
    li[num_1].append(num_2)
    li[num_2].append(num_1)

visited = [0] * (N + 1)

for i in range(1,N+1):
    li[i].sort()

dfs(li, V, visited)
print()
bfs(li, V, visited)



