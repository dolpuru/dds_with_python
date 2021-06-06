import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

array = []
visited = []
x_pattern = [1, -1, 0, 0]
y_pattern = [0, 0, 1, -1]


def bfs(i, j, height):
    global N,visited
    visited[i][j] = 1
    for k in range(4):
        i_ = i+x_pattern[k]
        j_ = j+y_pattern[k]
        if i_>=0 and j_>=0 and i_<N and j_<N and visited[i_][j_]==0 and array[i_][j_] > height:
            bfs(i_, j_, height)
            

def func():
    global N, visited
    ans = 0
    for height in range(1, 101):
        visited = [[0 for i in range(N)] for j in range(N)]
        count = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and array[i][j] > height:
                    count += 1
                    bfs(i, j, height)
        ans = max(count, ans)
    print(ans)

if __name__ == '__main__':
    global N
    N = int(input())
    for i in range(N):
        array.append(list(map(int, input().split(' '))))
    func()

