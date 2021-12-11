import sys
from collections import deque 

input = sys.stdin.readline

N = int(input())
array = [ [] for i in range(N+1)]
for i in range(N-1):
    v1, v2 = map(int, input().split(' '))
    array[v1].append(v2)
    array[v2].append(v1)

parent = [0 for i in range(N+1)]
queue = deque()
queue.append(1)
while queue:
    v = queue.popleft()
    for i in array[v]:
        if parent[i] == 0:
            parent[i] = v
            queue.append(i)
            
for i in range(2, N+1):
    print(parent[i])
