from collections import deque
n , m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(input())

#dfs + 하다가 막혀있으면 -1
visited = [list(False for _ in range(m)) for _ in range(n)]
count = 0
v = [0,0]
def dfs(maze,visited,v):
    maze[]
