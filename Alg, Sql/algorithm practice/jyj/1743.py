import sys
from collections import deque
input = sys.stdin.readline

k_list = []
visited = []
x_pattern = [1, -1, 0, 0]
y_pattern = [0, 0, 1, -1]
queue = deque()


def func(N, M):
    ans = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if visited[i][j] == 0 and k_list[i][j] == 1:
                queue.append([i, j])
                count = 0
                
                while queue:
                    x, y = map(int, queue.popleft())
                    
                    for k in range(4):
                        if x+x_pattern[k] >= 1 and y+y_pattern[k] >=1 and x+x_pattern[k] < N+1 and y+y_pattern[k] < M+1 and visited[x+x_pattern[k]][y+y_pattern[k]] == 0 and k_list[x+x_pattern[k]][y+y_pattern[k]] ==1:
                            queue.append([x+x_pattern[k], y+y_pattern[k]])
                            visited[x+x_pattern[k]][y+y_pattern[k]] = 1
                            count+=1
                ans = max(count, ans)
                    

    print(ans)
 

if __name__ == '__main__':
    N, M, K = map(int, input().split(' '))
    k_list = [[0 for i in range(M+1)] for j in range(N+1)]
    visited = [[0 for i in range(M+1)] for j in range(N+1)]
    for i in range(K):
        x, y = map(int, input().split(' '))
        k_list[x][y] = 1

    func(N, M)

